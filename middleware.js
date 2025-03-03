module.exports.isLoggedIn = (req,res,next)=>{
if(!req.isAuthenticated()){
req.flash("success","You don't have permission to access it");
return res.redirect("/login");
}
next();
};