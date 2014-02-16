// prettify
var j=!0,p=null,x=!1;window.PR_SHOULD_USE_CONTINUATION=j;function A(b,c,g,e){c&&(b={a:c,d:b},g(b),e.push.apply(e,b.e))}
function B(b,c){function g(b){for(var a=b.d,q=[a,"pln"],e=0,k=b.a.match(t)||[],E={},d=0,s=k.length;d<s;++d){var i=k[d],n=E[i],m=void 0,h;if("string"===typeof n)h=x;else{var l=v[i.charAt(0)];if(l)m=i.match(l[1]),n=l[0];else{for(h=0;h<f;++h)if(l=c[h],m=i.match(l[1])){n=l[0];break}m||(n="pln")}if((h=5<=n.length&&"lang-"===n.substring(0,5))&&!(m&&"string"===typeof m[1]))h=x,n="src";h||(E[i]=n)}l=e;e+=i.length;if(h){h=m[1];var r=i.indexOf(h),z=r+h.length;m[2]&&(z=i.length-m[2].length,r=z-h.length);n=n.substring(5);
A(a+l,i.substring(0,r),g,q);A(a+l+r,h,F(n,h),q);A(a+l+z,i.substring(z),g,q)}else q.push(a+l,n)}b.e=q}function e(b){for(var a=b.source.match(RegExp("(?:\\[(?:[^\\x5C\\x5D]|\\\\[\\s\\S])*\\]|\\\\u[A-Fa-f0-9]{4}|\\\\x[A-Fa-f0-9]{2}|\\\\[0-9]+|\\\\[^ux0-9]|\\(\\?[:!=]|[\\(\\)\\^]|[^\\x5B\\x5C\\(\\)\\^]+)","g")),q=a.length,f=[],k=0,e=0;k<q;++k){var d=a[k];"("===d?++e:"\\"===d.charAt(0)&&(d=+d.substring(1))&&(d<=e?f[d]=-1:a[k]=w(d))}for(k=1;k<f.length;++k)-1===f[k]&&(f[k]=++l);for(e=k=0;k<q;++k)d=a[k],
"("===d?(++e,f[e]||(a[k]="(?:")):"\\"===d.charAt(0)&&(d=+d.substring(1))&&d<=e&&(a[k]="\\"+f[d]);for(k=0;k<q;++k)"^"===a[k]&&"^"!==a[k+1]&&(a[k]="");if(b.ignoreCase&&r)for(k=0;k<q;++k)d=a[k],b=d.charAt(0),2<=d.length&&"["===b?a[k]=u(d):"\\"!==b&&(a[k]=d.replace(/[a-zA-Z]/g,function(a){a=a.charCodeAt(0);return"["+String.fromCharCode(a&-33,a|32)+"]"}));return a.join("")}function u(a){var d=a.substring(1,a.length-1).match(RegExp("\\\\u[0-9A-Fa-f]{4}|\\\\x[0-9A-Fa-f]{2}|\\\\[0-3][0-7]{0,2}|\\\\[0-7]{1,2}|\\\\[\\s\\S]|-|[^-\\\\]",
"g")),a=[],b="^"===d[0],f=["["];b&&f.push("^");for(var b=b?1:0,e=d.length;b<e;++b){var c=d[b];if(/\\[bdsw]/i.test(c))f.push(c);else{var c=D(c),g;b+2<e&&"-"===d[b+1]?(g=D(d[b+2]),b+=2):g=c;a.push([c,g]);65>g||122<c||(65>g||90<c||a.push([Math.max(65,c)|32,Math.min(g,90)|32]),97>g||122<c||a.push([Math.max(97,c)&-33,Math.min(g,122)&-33]))}}a.sort(function(a,b){return a[0]-b[0]||b[1]-a[1]});d=[];e=[];for(b=0;b<a.length;++b)c=a[b],c[0]<=e[1]+1?e[1]=Math.max(e[1],c[1]):d.push(e=c);for(b=0;b<d.length;++b)c=
d[b],f.push(w(c[0])),c[1]>c[0]&&(c[1]+1>c[0]&&f.push("-"),f.push(w(c[1])));f.push("]");return f.join("")}function w(a){if(32>a)return(16>a?"\\x0":"\\x")+a.toString(16);a=String.fromCharCode(a);return"\\"===a||"-"===a||"]"===a||"^"===a?"\\"+a:a}function D(a){var b=a.charCodeAt(0);if(92!==b)return b;var c=a.charAt(1);return(b=d[c])?b:"0"<=c&&"7">=c?parseInt(a.substring(1),8):"u"===c||"x"===c?parseInt(a.substring(2),16):a.charCodeAt(1)}for(var v={},t,m=b.concat(c),i=[],h={},y=0,a=m.length;y<a;++y){var n=
m[y],z=n[3];if(z)for(var s=z.length;0<=--s;)v[z.charAt(s)]=n;n=n[1];z=""+n;h.hasOwnProperty(z)||(i.push(n),h[z]=p)}i.push(/[\0-\uffff]/);for(var l=0,r=x,m=x,h=0,y=i.length;h<y;++h)if(a=i[h],a.ignoreCase)m=j;else if(/[a-z]/i.test(a.source.replace(/\\u[0-9a-f]{4}|\\x[0-9a-f]{2}|\\[^ux]/gi,""))){r=j;m=x;break}for(var d={b:8,t:9,n:10,v:11,f:12,r:13},n=[],h=0,y=i.length;h<y;++h){a=i[h];if(a.global||a.multiline)throw Error(""+a);n.push("(?:"+e(a)+")")}t=RegExp(n.join("|"),m?"gi":"g");var f=c.length;return g}
function G(b){var c=[],g=[];b.tripleQuotedStrings?c.push(["str",/^(?:\'\'\'(?:[^\'\\]|\\[\s\S]|\'{1,2}(?=[^\']))*(?:\'\'\'|$)|\"\"\"(?:[^\"\\]|\\[\s\S]|\"{1,2}(?=[^\"]))*(?:\"\"\"|$)|\'(?:[^\\\']|\\[\s\S])*(?:\'|$)|\"(?:[^\\\"]|\\[\s\S])*(?:\"|$))/,p,"'\""]):b.multiLineStrings?c.push(["str",/^(?:\'(?:[^\\\']|\\[\s\S])*(?:\'|$)|\"(?:[^\\\"]|\\[\s\S])*(?:\"|$)|\`(?:[^\\\`]|\\[\s\S])*(?:\`|$))/,p,"'\"`"]):c.push(["str",/^(?:\'(?:[^\\\'\r\n]|\\.)*(?:\'|$)|\"(?:[^\\\"\r\n]|\\.)*(?:\"|$))/,p,"\"'"]);b.verbatimStrings&&
g.push(["str",/^@\"(?:[^\"]|\"\")*(?:\"|$)/,p]);var e=b.hashComments;e&&(b.cStyleComments?(1<e?c.push(["com",/^#(?:##(?:[^#]|#(?!##))*(?:###|$)|.*)/,p,"#"]):c.push(["com",/^#(?:(?:define|e(?:l|nd)if|else|error|ifn?def|include|line|pragma|undef|warning)\b|[^\r\n]*)/,p,"#"]),g.push(["str",/^<(?:(?:(?:\.\.\/)*|\/?)(?:[\w-]+(?:\/[\w-]+)+)?[\w-]+\.h(?:h|pp|\+\+)?|[a-z]\w*)>/,p])):c.push(["com",/^#[^\r\n]*/,p,"#"]));b.cStyleComments&&(g.push(["com",/^\/\/[^\r\n]*/,p]),g.push(["com",/^\/\*[\s\S]*?(?:\*\/|$)/,
p]));b.regexLiterals&&g.push(["lang-regex",RegExp("^(?:^^\\.?|[+-]|[!=]=?=?|\\#|%=?|&&?=?|\\(|\\*=?|[+\\-]=|->|\\/=?|::?|<<?=?|>>?>?=?|,|;|\\?|@|\\[|~|{|\\^\\^?=?|\\|\\|?=?|break|case|continue|delete|do|else|finally|instanceof|return|throw|try|typeof)\\s*(/(?=[^/*])(?:[^/\\x5B\\x5C]|\\x5C[\\s\\S]|\\x5B(?:[^\\x5C\\x5D]|\\x5C[\\s\\S])*(?:\\x5D|$))+/)")]);(e=b.types)&&g.push(["typ",e]);b=(""+b.keywords).replace(/^ | $/g,"");b.length&&g.push(["kwd",RegExp("^(?:"+b.replace(/[\s,]+/g,"|")+")\\b"),p]);c.push(["pln",
/^\s+/,p," \r\n\t\u00a0"]);g.push(["lit",/^@[a-z_$][a-z_$@0-9]*/i,p],["typ",/^(?:[@_]?[A-Z]+[a-z][A-Za-z_$@0-9]*|\w+_t\b)/,p],["pln",/^[a-z_$][a-z_$@0-9]*/i,p],["lit",/^(?:0x[a-f0-9]+|(?:\d(?:_\d+)*\d*(?:\.\d*)?|\.\d\+)(?:e[+\-]?\d+)?)[a-z]*/i,p,"0123456789"],["pln",/^\\[\s\S]?/,p],["pun",/^.[^\s\w\.$@\'\"\`\/\\]*/,p]);return B(c,g)}
function L(b,c,g){function e(a){switch(a.nodeType){case 1:if(w.test(a.className))break;if("br"===a.nodeName)u(a),a.parentNode&&a.parentNode.removeChild(a);else for(a=a.firstChild;a;a=a.nextSibling)e(a);break;case 3:case 4:if(g){var b=a.nodeValue,c=b.match(D);if(c){var h=b.substring(0,c.index);a.nodeValue=h;(b=b.substring(c.index+c[0].length))&&a.parentNode.insertBefore(v.createTextNode(b),a.nextSibling);u(a);h||a.parentNode.removeChild(a)}}}}function u(a){function b(a,c){var e=c?a.cloneNode(x):a,
d=a.parentNode;if(d){var d=b(d,1),f=a.nextSibling;d.appendChild(e);for(var g=f;g;g=f)f=g.nextSibling,d.appendChild(g)}return e}for(;!a.nextSibling;)if(a=a.parentNode,!a)return;for(var a=b(a.nextSibling,0),c;(c=a.parentNode)&&1===c.nodeType;)a=c;m.push(a)}for(var w=/(?:^|\s)nocode(?:\s|$)/,D=/\r\n?|\n/,v=b.ownerDocument,t=v.createElement("li");b.firstChild;)t.appendChild(b.firstChild);for(var m=[t],i=0;i<m.length;++i)e(m[i]);c===(c|0)&&m[0].setAttribute("value",c);var h=v.createElement("ol");h.className=
"linenums";for(var c=Math.max(0,c-1|0)||0,i=0,y=m.length;i<y;++i)t=m[i],t.className="L"+(i+c)%10,t.firstChild||t.appendChild(v.createTextNode("\u00a0")),h.appendChild(t);b.appendChild(h)}function M(b,c){for(var g=c.length;0<=--g;){var e=c[g];N.hasOwnProperty(e)?O.console&&console.warn("cannot override language handler %s",e):N[e]=b}}function F(b,c){if(!b||!N.hasOwnProperty(b))b=/^\s*</.test(c)?"default-markup":"default-code";return N[b]}
function T(b){var c,g,e=b.g;try{var u=b.h,w=function(a){switch(a.nodeType){case 1:if(D.test(a.className))break;for(var b=a.firstChild;b;b=b.nextSibling)w(b);b=a.nodeName.toLowerCase();if("br"===b||"li"===b)v[i]="\n",m[i<<1]=t++,m[i++<<1|1]=a;break;case 3:case 4:b=a.nodeValue,b.length&&(b=u?b.replace(/\r\n?/g,"\n"):b.replace(/[ \t\r\n]+/g," "),v[i]=b,m[i<<1]=t,t+=b.length,m[i++<<1|1]=a)}},D=/(?:^|\s)nocode(?:\s|$)/,v=[],t=0,m=[],i=0;w(b.c);c=v.join("").replace(/\n$/,"");g=m;b.a=c;b.j=g;b.d=0;F(e,c)(b);
var h=/\bMSIE\s(\d+)/.exec(navigator.userAgent),h=h&&8>=+h[1];c=/\n/g;var y=b.a,a=y.length;g=0;var n=b.j,z=n.length,e=0,s=b.e,l=s.length,r=0;s[l]=a;var d,f;for(f=d=0;f<l;)s[f]!==s[f+2]?(s[d++]=s[f++],s[d++]=s[f++]):f+=2;l=d;for(f=d=0;f<l;){for(var da=s[f],P=s[f+1],q=f+2;q+2<=l&&s[q+1]===P;)q+=2;s[d++]=da;s[d++]=P;f=q}s.length=d;var H=b.c,k;H&&(k=H.style.display,H.style.display="none");try{for(;e<z;){var E=n[e+2]||a,Q=s[r+2]||a,q=Math.min(E,Q),C=n[e+1],I;if(1!==C.nodeType&&(I=y.substring(g,q))){h&&
(I=I.replace(c,"\r"));C.nodeValue=I;var R=C.ownerDocument,J=R.createElement("span");J.className=s[r+1];var S=C.parentNode;S.replaceChild(J,C);J.appendChild(C);g<E&&(n[e+1]=C=R.createTextNode(y.substring(q,E)),S.insertBefore(C,J.nextSibling))}g=q;g>=E&&(e+=2);g>=Q&&(r+=2)}}finally{H&&(H.style.display=k)}}catch(K){O.console&&console.log(K&&K.stack?K.stack:K)}}
var O=window,U=["break,continue,do,else,for,if,return,while"],V=[[U,"auto,case,char,const,default,double,enum,extern,float,goto,int,long,register,short,signed,sizeof,static,struct,switch,typedef,union,unsigned,void,volatile"],"catch,class,delete,false,import,new,operator,private,protected,public,this,throw,true,try,typeof"],W=[V,"alignof,align_union,asm,axiom,bool,concept,concept_map,const_cast,constexpr,decltype,dynamic_cast,explicit,export,friend,inline,late_check,mutable,namespace,nullptr,reinterpret_cast,static_assert,static_cast,template,typeid,typename,using,virtual,where"],
X=[V,"abstract,boolean,byte,extends,final,finally,implements,import,instanceof,null,native,package,strictfp,super,synchronized,throws,transient"],Y=[X,"as,base,by,checked,decimal,delegate,descending,dynamic,event,fixed,foreach,from,group,implicit,in,interface,internal,into,is,let,lock,object,out,override,orderby,params,partial,readonly,ref,sbyte,sealed,stackalloc,string,select,uint,ulong,unchecked,unsafe,ushort,var,virtual,where"],Z=[V,"debugger,eval,export,function,get,null,set,undefined,var,with,Infinity,NaN"],
$=[U,"and,as,assert,class,def,del,elif,except,exec,finally,from,global,import,in,is,lambda,nonlocal,not,or,pass,print,raise,try,with,yield,False,True,None"],aa=[U,"alias,and,begin,case,class,def,defined,elsif,end,ensure,false,in,module,next,nil,not,or,redo,rescue,retry,self,super,then,true,undef,unless,until,when,yield,BEGIN,END"],ba=[U,"case,done,elif,esac,eval,fi,function,in,local,set,then,until"],ca=/^(DIR|FILE|vector|(de|priority_)?queue|list|stack|(const_)?iterator|(multi)?(set|map)|bitset|u?(int|float)\d*)\b/,
ea=/\S/,fa=G({keywords:[W,Y,Z,"caller,delete,die,do,dump,elsif,eval,exit,foreach,for,goto,if,import,last,local,my,next,no,our,print,package,redo,require,sub,undef,unless,until,use,wantarray,while,BEGIN,END"+$,aa,ba],hashComments:j,cStyleComments:j,multiLineStrings:j,regexLiterals:j}),N={};M(fa,["default-code"]);
M(B([],[["pln",/^[^<?]+/],["dec",/^<!\w[^>]*(?:>|$)/],["com",/^<\!--[\s\S]*?(?:-\->|$)/],["lang-",/^<\?([\s\S]+?)(?:\?>|$)/],["lang-",/^<%([\s\S]+?)(?:%>|$)/],["pun",/^(?:<[%?]|[%?]>)/],["lang-",/^<xmp\b[^>]*>([\s\S]+?)<\/xmp\b[^>]*>/i],["lang-js",/^<script\b[^>]*>([\s\S]*?)(<\/script\b[^>]*>)/i],["lang-css",/^<style\b[^>]*>([\s\S]*?)(<\/style\b[^>]*>)/i],["lang-in.tag",/^(<\/?[a-z][^<>]*>)/i]]),"default-markup htm html mxml xhtml xml xsl".split(" "));
M(B([["pln",/^[\s]+/,p," \t\r\n"],["atv",/^(?:\"[^\"]*\"?|\'[^\']*\'?)/,p,"\"'"]],[["tag",/^^<\/?[a-z](?:[\w.:-]*\w)?|\/?>$/i],["atn",/^(?!style[\s=]|on)[a-z](?:[\w:-]*\w)?/i],["lang-uq.val",/^=\s*([^>\'\"\s]*(?:[^>\'\"\s\/]|\/(?=\s)))/],["pun",/^[=<>\/]+/],["lang-js",/^on\w+\s*=\s*\"([^\"]+)\"/i],["lang-js",/^on\w+\s*=\s*\'([^\']+)\'/i],["lang-js",/^on\w+\s*=\s*([^\"\'>\s]+)/i],["lang-css",/^style\s*=\s*\"([^\"]+)\"/i],["lang-css",/^style\s*=\s*\'([^\']+)\'/i],["lang-css",/^style\s*=\s*([^\"\'>\s]+)/i]]),
["in.tag"]);M(B([],[["atv",/^[\s\S]+/]]),["uq.val"]);M(G({keywords:W,hashComments:j,cStyleComments:j,types:ca}),"c cc cpp cxx cyc m".split(" "));M(G({keywords:"null,true,false"}),["json"]);M(G({keywords:Y,hashComments:j,cStyleComments:j,verbatimStrings:j,types:ca}),["cs"]);M(G({keywords:X,cStyleComments:j}),["java"]);M(G({keywords:ba,hashComments:j,multiLineStrings:j}),["bsh","csh","sh"]);M(G({keywords:$,hashComments:j,multiLineStrings:j,tripleQuotedStrings:j}),["cv","py"]);
M(G({keywords:"caller,delete,die,do,dump,elsif,eval,exit,foreach,for,goto,if,import,last,local,my,next,no,our,print,package,redo,require,sub,undef,unless,until,use,wantarray,while,BEGIN,END",hashComments:j,multiLineStrings:j,regexLiterals:j}),["perl","pl","pm"]);M(G({keywords:aa,hashComments:j,multiLineStrings:j,regexLiterals:j}),["rb"]);M(G({keywords:Z,cStyleComments:j,regexLiterals:j}),["js"]);
M(G({keywords:"all,and,by,catch,class,else,extends,false,finally,for,if,in,is,isnt,loop,new,no,not,null,of,off,on,or,return,super,then,throw,true,try,unless,until,when,while,yes",hashComments:3,cStyleComments:j,multilineStrings:j,tripleQuotedStrings:j,regexLiterals:j}),["coffee"]);M(B([],[["str",/^[\s\S]+/]]),["regex"]);
var ga=O.PR={createSimpleLexer:B,registerLangHandler:M,sourceDecorator:G,PR_ATTRIB_NAME:"atn",PR_ATTRIB_VALUE:"atv",PR_COMMENT:"com",PR_DECLARATION:"dec",PR_KEYWORD:"kwd",PR_LITERAL:"lit",PR_NOCODE:"nocode",PR_PLAIN:"pln",PR_PUNCTUATION:"pun",PR_SOURCE:"src",PR_STRING:"str",PR_TAG:"tag",PR_TYPE:"typ",prettyPrintOne:O.prettyPrintOne=function(b,c,g){var e=document.createElement("pre");e.innerHTML=b;g&&L(e,g,j);T({g:c,i:g,c:e,h:1});return e.innerHTML},prettyPrint:O.prettyPrint=function(b){function c(){for(var g=
O.PR_SHOULD_USE_CONTINUATION?v.now()+250:Infinity;t<e.length&&v.now()<g;t++){var l=e[t],r=l.className;if(h.test(r)&&!y.test(r)){for(var d=x,f=l.parentNode;f;f=f.parentNode)if(z.test(f.tagName)&&f.className&&h.test(f.className)){d=j;break}if(!d){l.className+=" prettyprinted";var r=r.match(i),w;if(d=!r){for(var d=l,f=void 0,u=d.firstChild;u;u=u.nextSibling)var q=u.nodeType,f=1===q?f?d:u:3===q?ea.test(u.nodeValue)?d:f:f;d=(w=f===d?void 0:f)&&n.test(w.tagName)}d&&(r=w.className.match(i));r&&(r=r[1]);
d=a.test(l.tagName)?1:(d=(d=l.currentStyle)?d.whiteSpace:document.defaultView&&document.defaultView.getComputedStyle?document.defaultView.getComputedStyle(l,p).getPropertyValue("white-space"):0)&&"pre"===d.substring(0,3);(f=(f=l.className.match(/\blinenums\b(?::(\d+))?/))?f[1]&&f[1].length?+f[1]:j:x)&&L(l,f,d);m={g:r,c:l,i:f,h:d};T(m)}}}t<e.length?setTimeout(c,250):b&&b()}for(var g=[document.getElementsByTagName("pre"),document.getElementsByTagName("code"),document.getElementsByTagName("xmp")],e=
[],u=0;u<g.length;++u)for(var w=0,D=g[u].length;w<D;++w)e.push(g[u][w]);var g=p,v=Date;v.now||(v={now:function(){return+new Date}});var t=0,m,i=/\blang(?:uage)?-([\w.]+)(?!\S)/,h=/\bprettyprint\b/,y=/\bprettyprinted\b/,a=/pre|xmp/i,n=/^code$/i,z=/^(?:pre|code|xmp)$/i;c()}};"function"===typeof define&&define.amd&&define("google-code-prettify",[],function(){return ga});
// prettyprint css
PR.registerLangHandler(PR.createSimpleLexer([[PR.PR_PLAIN,/^[ \t\r\n\f]+/,null," \t\r\n\f"]],[[PR.PR_STRING,/^\"(?:[^\n\r\f\\\"]|\\(?:\r\n?|\n|\f)|\\[\s\S])*\"/,null],[PR.PR_STRING,/^\'(?:[^\n\r\f\\\']|\\(?:\r\n?|\n|\f)|\\[\s\S])*\'/,null],["lang-css-str",/^url\(([^\)\"\']+)\)/i],[PR.PR_KEYWORD,/^(?:url|rgb|\!important|@import|@page|@media|@charset|inherit)(?=[^\-\w]|$)/i,null],["lang-css-kw",/^(-?(?:[_a-z]|(?:\\[0-9a-f]+ ?))(?:[_a-z0-9\-]|\\(?:\\[0-9a-f]+ ?))*)\s*:/i],[PR.PR_COMMENT,/^\/\*[^*]*\*+(?:[^\/*][^*]*\*+)*\//],
[PR.PR_COMMENT,/^(?:<\!--|--\>)/],[PR.PR_LITERAL,/^(?:\d+|\d*\.\d+)(?:%|[a-z]+)?/i],[PR.PR_LITERAL,/^#(?:[0-9a-f]{3}){1,2}/i],[PR.PR_PLAIN,/^-?(?:[_a-z]|(?:\\[\da-f]+ ?))(?:[_a-z\d\-]|\\(?:\\[\da-f]+ ?))*/i],[PR.PR_PUNCTUATION,/^[^\s\w\'\"]+/]]),["css"]);PR.registerLangHandler(PR.createSimpleLexer([],[[PR.PR_KEYWORD,/^-?(?:[_a-z]|(?:\\[\da-f]+ ?))(?:[_a-z\d\-]|\\(?:\\[\da-f]+ ?))*/i]]),["css-kw"]);PR.registerLangHandler(PR.createSimpleLexer([],[[PR.PR_STRING,/^[^\)\"\']+/]]),["css-str"]);

//' wordpress thread comment
addComment={moveForm:function(d,f,i,c){var m=this,a,h=m.I(d),b=m.I(i),l=m.I("cancel-comment-reply-link"),j=m.I("comment_parent"),k=m.I("comment_post_ID");if(!h||!b||!l||!j){return}m.respondId=i;c=c||false;if(!m.I("wp-temp-form-div")){a=document.createElement("div");a.id="wp-temp-form-div";a.style.display="none";b.parentNode.insertBefore(a,b)}h.parentNode.insertBefore(b,h.nextSibling);if(k&&c){k.value=c}j.value=f;l.style.display="";l.onclick=function(){var n=addComment,e=n.I("wp-temp-form-div"),o=n.I(n.respondId);if(!e||!o){return}n.I("comment_parent").value="0";e.parentNode.insertBefore(o,e);e.parentNode.removeChild(e);this.style.display="none";this.onclick=null;return false};try{m.I("comment").focus()}catch(g){}return false},I:function(a){return document.getElementById(a)}};

// 90dues
;(function($){
  // init PrettyPrint
  window.prettyPrint && prettyPrint();

  // HTML5 Placeholder
  if(!Modernizr.input.placeholder){$("[placeholder]").focus(function(){var input=$(this);if(input.val()==input.attr("placeholder")){input.val("");input.removeClass("placeholder")}}).blur(function(){var input=$(this);if(input.val()==""||input.val()==input.attr("placeholder")){input.addClass("placeholder");input.val(input.attr("placeholder"))}}).blur();$("[placeholder]").parents("form").submit(function(){$(this).find("[placeholder]").each(function(){var input=$(this);if(input.val()==input.attr("placeholder"))input.val("")})})};

  // prevent nav click
  $(".pagination a[href^=#]").on("click", !1);
  
  // replying comment on non touch device
  var commentidentity = $('.comment-identity,#submit'), 
      commentarea  = $('#comment');
  if(!Modernizr.touch){
    commentidentity.hide();
    commentarea.on('focus',function(){
      $(this).animate({
        'height':'200px'
      }, function(){
        commentidentity.slideDown()
      })
    });
  } else {
    //footer widget toggler for touch device
    $('.footer-widget h3').on('click', function(){
      $(this).parent().toggleClass('open')
    });
  }

  // better comment
  $('.reply').on('click','.comment-reply-link', function(){
    var usrName = $(this).parents('article').find('.fn').text(),
        usrID = $(this).parents('article').attr('id'),
        usrBoxPosition = $(this).parents('article');
    commentarea.val('<a href="#'+usrID+'">@'+usrName+"</a>, ");
    $("html,body").animate({
        scrollTop: usrBoxPosition.offset().top
    }, "slow")
  })
  $('#cancel-comment-reply-link').on('click', function(){
    commentarea.val("");
  })

// comment click anchor links
$('.comment-content').on('click', 'a[href^="#comment-"]', function(){
  var anchor_offsetop = $(this).attr('href');
      comment_linkpos = $(anchor_offsetop).offset().top;
  $('html, body').animate({ 
    scrollTop: comment_linkpos
  },500);  
  return!1
});

  // navbar search form
  var serchBtn = $(".navbar .search a");
  $(".navbar .search a, .navbar #close-search").on("click", function() {
    $(".navbar .searchform-li").slideToggle("fast", function() {
      $("#gi").focus()
    });
    $(".navbar").toggleClass("open");
    return!1
  });

  // better explaination on <pre>
  $(".entry-content pre").find('del').attr("title", "deleted");
  $(".entry-content pre").find('ins').attr("title", "inserted");

  // ajax search
  function makeAjaxSearch(result) {
    if(result.length) {
      $("#search_filtered").empty().show();
      for (var i = 0; i < result.length - 1; i++) {
        $("#search_filtered").append('<li><a href="' + result[i]["url"] + '">' + result[i]["title"] + '</a></li>');
      }
    }else {
      $("#search_filtered").show().html('<li><a id="search-error" href="javascript:void(0);">Not Found. Try another keyword.</a></li>')
    }
  }
  var delaySearch;
  function startSearch() {
    $.ajax({
      type:'GET',
      url:'/', // hard code blog url
      data:'s=' + $('#s').val(),
      dataType:'json',
      success: function(result){
        makeAjaxSearch(result)
			}
  	});
	}
  $('#s').on('keyup',function(e) {
      if ( $('#s').val() && e.keyCode != 13) {
        if (delaySearch) {
            clearTimeout(delaySearch)
        }
        delaySearch = setTimeout(startSearch, 200);
      } else 
        $('#search_filtered').hide().empty();
    });
  $("#search_filtered").on("click", "#search-error", function() {
    $("#s").focus().select()
  });
  $('#s').on("keydown", function(event){
    if(event.keyCode == 13) {
      event.preventDefault();
      return false;
    }
  })

  //scroll top
  $("#gotop").on("click", function() {$(document).scrollTop(0); return!1 });
})(window.jQuery);