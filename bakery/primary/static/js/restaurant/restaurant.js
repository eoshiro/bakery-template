// Navbar Scroll

$(window).on('scroll',function(){
if ($(window).scrollTop()){
    $('.ttw-base-mainnavbar').addClass('ttw-base-scrolledblack');
    $('.ttw-base-mainnavbar').removeClass('.ttw-base-navbar');
  }
  else
    {
      $('nav').removeClass('ttw-base-scrolledblack');
    }
  })

  $(window).on('scroll',function(){
  if ($(window).scrollTop()){
      $('.logotop').addClass('ttw-base-logotop-white');
      $('.logotop').removeClass('.ttw-base-logotop');
    }
    else
      {
        $('img').removeClass('ttw-base-logotop-white');
      }
    })

    $(window).on('scroll',function(){
    if ($(window).scrollTop()){
        $('.logowords').addClass('ttw-base-logowords-white');
        $('.logowords').removeClass('.ttw-base-logowords');
      }
      else
        {
          $('div').removeClass('ttw-base-logowords-white');
        }
      })

      $(window).on('scroll',function(){
      if ($(window).scrollTop()){
          $('.base-hamburger-topnav').addClass('base-topnav-white');
          $('.base-hamburger-topnav').removeClass('.remove');
        }
        else
          {
            $('div').removeClass('base-topnav-white');
          }
        })
  /* Toggle between showing and hiding the navigation menu links when the user clicks on the hamburger menu / bar icon */
function hamburgerFunctionBase() {
  var x = document.getElementById("navbar-header-links");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

function hamburgerFunctionLinksOne() {
  var x = document.getElementById("background-links-coding");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

function hamburgerFunctionLinksTwo() {
  var x = document.getElementById("background-links-branding");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

function hamburgerFunctionLinksFront() {
  var x = document.getElementById("background-links-front");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}

function hamburgerFunctionLinksBack() {
  var x = document.getElementById("background-links-back");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}
