!function(e){var t={};function n(o){if(t[o])return t[o].exports;var r=t[o]={i:o,l:!1,exports:{}};return e[o].call(r.exports,r,r.exports,n),r.l=!0,r.exports}n.m=e,n.c=t,n.d=function(e,t,o){n.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:o})},n.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},n.t=function(e,t){if(1&t&&(e=n(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var o=Object.create(null);if(n.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)n.d(o,r,function(t){return e[t]}.bind(null,r));return o},n.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return n.d(t,"a",t),t},n.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},n.p="",n(n.s=0)}([function(e,t,n){"use strict";function o(){var e=document.querySelector("#snackbar");e.style.opacity=0,e.style.transform="translate(0,100%)",e.classList.remove("bg-gray-200","text-blue-700"),e.classList.add("bg-gray-900","text-gray-100")}function r(e){var t=document.querySelector("#snackbar");t.textContent=e,t.style.opacity=1,t.style.transform="translate(0,0)",setTimeout(o,2e3)}function c(e,t){var n=e.target.getBoundingClientRect(),o=document.querySelector("#tooltip");o.style.opacity=.6,o.style.visibility="visible",o.style.top=n.y+n.height+1+"px",o.style.left=n.x-4+"px",o.textContent=t}var a,u,l,i,d,s,f,m,y,p,v,g,b;n.r(t),a=document.querySelector('aside[role="navigation"]'),u=document.querySelector("#closeNavBtn"),(l=document.querySelector("#openNavBtn"))&&(l.onclick=function(){a.setAttribute("data-menu","open")}),u&&(u.onclick=function(){a.setAttribute("data-menu","closed")}),document.querySelectorAll(".nav-toc li.current a").forEach((function(e){u.offsetWidth>0&&u.offsetHeight>0&&(e.onclick=function(){a.setAttribute("data-menu","closed")})})),i=document.querySelector("#search-pane"),d=document.querySelector("#openSearchBtn"),s=document.querySelector("#closeSearchBtn"),d&&(d.onclick=function(){i.setAttribute("data-menu","open")}),s&&(s.onclick=function(){i.setAttribute("data-menu","closed")}),setTimeout((function(){var e=document.querySelector("#snackbar"),t=document.querySelectorAll(".highlighted"),n=document.querySelector("#search-input");t.length&&(e.innerHTML='<a class="tracking-wide" href="javascript:Documentation.hideSearchWords()">'+_("Clear highlighted words")+"</a>",e.classList.remove("bg-gray-900","text-gray-100"),e.classList.add("bg-gray-200","text-blue-700"),e.style.opacity=1,e.style.transform="translate(0,0)",document.querySelector("#snackbar > a").onclick=function(){o(),n.value=""},n.value=t[0].textContent,n.onsearch=function(){Documentation.hideSearchWords(),o()})}),500),f=document.querySelector("#searchbox"),m=document.querySelector("#search-input"),f.onsubmit=function(e){m.value.length<1&&e.preventDefault()},window.addEventListener("keydown",(function(e){"Slash"===e.code&&(m.focus(),m.value="",e.preventDefault()),"Escape"===e.code&&(m.blur(),e.preventDefault())})),y=document.querySelector("#tooltip"),window.onscroll=function(){y.textContent="",y.style.opacity=0,y.style.visibility="hidden"},document.querySelectorAll("button.copy").forEach((function(e){["mouseenter","focus"].forEach((function(t){e.addEventListener(t,(function(e){var t=e.target.getAttribute("aria-label");c(e,t)}))})),["mouseleave","blur"].forEach((function(t){e.addEventListener(t,(function(){}))})),e.onclick=function(){var t=function(e){var t=window.getSelection(),n=document.createRange();return n.selectNodeContents(e),t.removeAllRanges(),t.addRange(n),t}(e.parentNode);document.execCommand("copy"),t.removeAllRanges(),r(_("Copied code to clipboard"))}})),document.querySelectorAll(".headerlink").forEach((function(e){["mouseenter","focus"].forEach((function(t){e.addEventListener(t,(function(e){var t=e.target.getAttribute("data-title");c(e,t)}))})),["mouseleave","blur"].forEach((function(t){e.addEventListener(t,(function(){}))})),e.onclick=function(t){!function(e,t){var n=document.createElement("textarea");n.value=e,n.setAttribute("readonly",""),n.style.position="absolute",n.style.left="-9999px",document.body.appendChild(n);var o=document.getSelection().rangeCount>0&&document.getSelection().getRangeAt(0);n.select(),document.execCommand("copy"),document.body.removeChild(n),o&&(document.getSelection().removeAllRanges(),document.getSelection().addRange(o)),r(t)}(e.href,_("Copied link to clipboard")),t.preventDefault()}})),document.querySelectorAll(".expand").forEach((function(e){e.onclick=function(){e.parentElement.parentElement.classList.toggle("expanded")}})),document.querySelectorAll(".nav-toc a").forEach((function(e){e.onfocus=function(e){document.querySelectorAll(".expand").forEach((function(t){var n=t.parentElement.parentElement;n.contains(e.target)?n.classList.add("expanded"):n.classList.contains("current")||n.classList.remove("expanded")}))}})),p=document.querySelector("#main-wrapper"),v=p.offsetTop,g=document.documentElement.offsetHeight||document.body.offsetHeight,b=document.querySelectorAll("main section"),p.onscroll=function(){for(var e=0;e<b.length;++e){var t=b[e].getBoundingClientRect();if(v<=t.top&&t.top<=g){var n=document.querySelector(".nav-toc a[href*=".concat(b[e].id,"]"));n&&n.classList.add("current")}if(t.top<v||t.top>g){var o=document.querySelector(".nav-toc a[href*=".concat(b[e].id,"]"));o&&o.classList.remove("current")}}}}]);
