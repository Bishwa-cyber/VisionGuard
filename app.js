const express = require("express");
const ffmpeg = require('fluent-ffmpeg');
const app = express();
const port = 8080;
const path = require("path");
const mongoose = require("mongoose");
const engiene = require("ejs-mate");

const ExpressError = require("./utils/ExpressError.js");
const wrapasync = require("./utils/wrapasync.js");

const session = require("express-session");
const flash = require("connect-flash");
const passport = require("passport");
const localstrategy = require("passport-local");
const user = require("./models/user.js");
const { isLoggedIn } = require("./middleware.js");

app.set("view engine","ejs");
app.set("views",path.join(__dirname,"/views"));
app.engine("ejs",engiene);

app.use(express.static(path.join(__dirname,"/public")));
app.use(express.urlencoded({extended:true}));
app.use(express.json());

async function main() {
    await mongoose.connect("mongodb://127.0.0.1:27017/securityagency");
}

main()
.then(()=>{
    console.log("connected");
})
.catch((err)=>{
    console.log(err);
})
;

const sessionoption = {
    secret : "asdfgh",
    resave : false,
    saveUninitialized : true,
    cookie:{
        expires : Date.now()+7*24*60*60*1000,
        maxAge : 7*24*60*60*1000,
        httpOnly : true
    }
};

app.use(session(sessionoption));
app.use(flash());

app.use(passport.initialize());
app.use(passport.session());
passport.use(new localstrategy(user.authenticate()));
passport.serializeUser(user.serializeUser());
passport.deserializeUser(user.deserializeUser());

app.use((req,res,next)=>{
    res.locals.success = req.flash("success");
    res.locals.error = req.flash("error");
    res.locals.currentUser = req.user;
    next();
});

app.get("/security",(req,res)=>{
  res.render("content/index.ejs");
});

// Dashboard route to render EJS and display the video

app.get("/dashboard",isLoggedIn,(req,res)=>{
    res.sendFile(path.join(__dirname, "views", "dashboard.html"));
});
app.get("/signup",(req,res)=>{
    res.render("user/signup.ejs");
});
app.post("/signup",wrapasync(async(req,res,next)=>{
    try{
        let {username,email,password} = req.body;
    const newuser = new user({
        username : username,
        email:email
    });
    const registereduser = await user.register(newuser,password);
    req.login(registereduser,(err)=>{
        if(err){
            return next(err);
        }
        req.flash("success","Welcome to SecureWorld");
        res.redirect("/dashboard");
       });
    }
    catch(error){
      req.flash("error","given username already exitst");
      res.redirect("/signup");
    }
}));
app.get("/login",(req,res)=>{
    res.render("user/login.ejs");
});
app.post("/login",passport.authenticate("local",{
    failureRedirect:"/login",
    failureFlash:true
}),(req,res)=>{
    req.flash("success",("welcome come back to Secure World"));
    res.redirect("/dashboard");
});
app.get("/logout",async(req,res)=>{
req.logout((err)=>{
    if(err){
        return next(err);
    }
    req.flash("success","you logged out successfully");
    res.redirect("/security");
});
});
app.get("/footage1",(req,res)=>{
    res.render("content/footage1.ejs",{videoUrl:"/videos/pp456.mp4"});
});
app.get("/footage2",(req,res)=>{
    res.render("content/footage2.ejs",{videoUrl:"/videos/pp8.mp4"});
});
app.all("*",(req,res,next)=>{
    throw new ExpressError(404,"page not found");
});
app.use((err,req,res,next)=>{
    let {status = 500,message = "internal server error"} = err;
    res.status(status).render("content/error.ejs",{message});
});
app.listen(port,()=>{
    console.log("listening");
});