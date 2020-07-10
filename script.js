document.addEventListener("DOMContentLoaded", function() {

    software = ['android', 'apache', 'archlinux', 'ardour', 'asciinema',
                'awesomewm', 'coffeescript', 'concourse', 'css3', 'c',
                'debian', 'duolingo', 'firefox', 'flask', 'freebsd', 'gimp',
                'github', 'gnuicecat', 'gnu', 'html5', 'imgur', 'inkscape',
                'jupyter', 'krita', 'last-dot-fm', 'latex', 'linux', 'lmms',
                'mozilla', 'musescore', 'mysql', 'obsstudio', 'openbsd',
                'opensourceinitiative', 'openssl', 'php', 'pypi', 'python',
                'reddit', 'repl-dot-it', 'rust', 'sega', 'simpleicons',
                'soundcloud', 'sqlite', 'stylus', 'tor', 'tunein', 'twitch',
                'ubuntu', 'unity', 'vim', 'wechat', 'wikipedia', 'wordpress',
                'x-dot-org']
 //       ['awesomewm', 'archlinux']

    /*software.forEach(function(simpleicon){

    document.body.innerHTML += `
    <div class="box">
      <div class="badge ${simpleicon}-badge">
        <div class="left ${simpleicon}-left"><img src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/${simpleicon}.svg" /></div>
        <div class="right ${simpleicon}-right">${simpleicon}</div>
      </div>
    </div>
`
  })  */

  //document.querySelector("body").addEventListener("click", function() {
    //["object", "iframe", "embed", "img"].forEach(function(elmtType) {
      //var e, threeElmts = document.querySelectorAll(elmtType);
      var all_img = document.querySelectorAll("img");
      //e = threeElmts[0];
      all_img.forEach(function(e){
      //e = all_img[0];
      if (e.contentDocument) e.parentElement.replaceChild(e.contentDocument.documentElement.cloneNode(true), e);
      //e = threeElmts[1];
      //if (e.getSVGDocument) e.parentElement.replaceChild(e.getSVGDocument().documentElement.cloneNode(true), e);
      //e = threeElmts[2];
      var xhr = new XMLHttpRequest();
      xhr.open("GET", e.getAttribute(e.nodeName === "OBJECT" ? "data" : "src"));
      xhr.send();
      xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) e.outerHTML = xhr.responseText;
      };
     });
    //});
  //});


});
