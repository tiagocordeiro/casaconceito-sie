var $jscomp={scope:{},findInternal:function(a,c,b){a instanceof String&&(a=String(a));for(var d=a.length,e=0;e<d;e++){var f=a[e];if(c.call(b,f,e,a))return{i:e,v:f}}return{i:-1,v:void 0}}};$jscomp.defineProperty="function"==typeof Object.defineProperties?Object.defineProperty:function(a,c,b){if(b.get||b.set)throw new TypeError("ES3 does not support getters and setters.");a!=Array.prototype&&a!=Object.prototype&&(a[c]=b.value)};
$jscomp.getGlobal=function(a){return"undefined"!=typeof window&&window===a?a:"undefined"!=typeof global&&null!=global?global:a};$jscomp.global=$jscomp.getGlobal(this);$jscomp.polyfill=function(a,c,b,d){if(c){b=$jscomp.global;a=a.split(".");for(d=0;d<a.length-1;d++){var e=a[d];e in b||(b[e]={});b=b[e]}a=a[a.length-1];d=b[a];c=c(d);c!=d&&null!=c&&$jscomp.defineProperty(b,a,{configurable:!0,writable:!0,value:c})}};
$jscomp.polyfill("Array.prototype.find",function(a){return a?a:function(a,b){return $jscomp.findInternal(this,a,b).v}},"es6-impl","es3");
(function(a){a(document).ready(function(){a("fieldset.collapse").each(function(c,b){0===a(b).find("div.errors").length&&a(b).addClass("collapsed").find("h2").first().append(' (<a id="fieldsetcollapser'+c+'" class="collapse-toggle" href="#">'+gettext("Show")+"</a>)")});a("fieldset.collapse a.collapse-toggle").click(function(c){a(this).closest("fieldset").hasClass("collapsed")?a(this).text(gettext("Hide")).closest("fieldset").removeClass("collapsed").trigger("show.fieldset",[a(this).attr("id")]):a(this).text(gettext("Show")).closest("fieldset").addClass("collapsed").trigger("hide.fieldset",
[a(this).attr("id")]);return!1})})})(django.jQuery);
