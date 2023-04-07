//slider 

var counter = 1;
setInterval(function(){
  document.getElementById('radio' + counter).checked = true;
  counter++;
  if(counter > 4){
    counter = 1;
  }
}, 5000);



//scroll to top button

  /*
   * - Define variables
   * - Calculate the document height and set the offset to a quarter of that value
   * - Add the event listeners for scroll and click
   */
   let btt = document.getElementById('back-to-top'),
      body = document.body,
      menubar = document.querySelector('#menu-bar'),
      nav = document.querySelector('.navbar'),
      docElem = document.documentElement,
      offset = 100,
      isChrome = navigator.userAgent.toLowerCase().indexOf('chrome') > -1,
      isFirefox = navigator.userAgent.toLowerCase().indexOf('firefox') > -1,
      isfEdege= navigator.userAgent.toLowerCase().indexOf('edge') > -1,
      isSafari = navigator.userAgent.toLowerCase().indexOf('Safari') > -1,
      isExplorer = navigator.userAgent.toLowerCase().indexOf('explorer') > -1,
      scrollPos, docHeight;
      




  // Call back function for when you reach the partucular ofset of your choice by calculating the document height
  docHeight = Math.max(body.scrollHeight, body.offsetHeight, docElem.clientHeight, docElem.scrollHeight, docElem.offsetHeight);
  if (docHeight != 'undefined') {
      offset = docHeight / 6;
  }

  // scroll event listener
  window.addEventListener('scroll', function() {

// back to top scroll function

  scrollPos = body.scrollTop || docElem.scrollTop;

  btt.className = (scrollPos > offset) ? 'visible' : '';


});

// Add click event listener
btt.addEventListener('click', function() {
  event.preventDefault();

  if (isFirefox, isChrome) {
      docElem.scrollTop = 0;
  } else {
      body.scrollTop = 0;
  }
});


//Scroll reveal animations
//Common reveal options to create reveal animations
const sr = ScrollReveal ({
  distance : '45px',
  duration : 2700,
  reset : true,
})



sr.reveal('.main-home',{ delay:350, origin:'left' })
sr.reveal('.qulity-image',{ delay:350, origin:'right' })
sr.reveal('.gallery',{ delay:350, origin:'top' })
sr.reveal('.menu-food-content',{ delay:350, origin:'top' })
sr.reveal('.menu-food-text',{ delay:350, origin:'bottom' })
sr.reveal('.enjoy-our-food',{ delay:350, origin:'bottom' })

sr.reveal('.footer-logo',{ delay:350, origin:'bottom' })



// section - Modal

const portfolioModals = document.querySelectorAll(".porfolio-model");
const imgCards = document.querySelectorAll(".img-card");
const portfolioCloseBtns = document.querySelectorAll(".portfolio-close-btn");

var portfolioModal = function (modalClick) {
  portfolioModals[modalClick].classList.add("active");
}

imgCards.forEach((imgCard, i) => {
  imgCard.addEventListener("click", () => {
      portfolioModal(i);
  });
});

portfolioCloseBtns.forEach((portfolioCloseBtn) => {
  portfolioCloseBtn.addEventListener("click", () => {
      portfolioModals.forEach((portfolioModalView) => {
          portfolioModalView.classList.remove("active");
      });
  });
});

const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').forEach(link => {
if(link.href.includes(`${activePage}`)){
  link.classList.add('active');
  console.log(link);
}
})

// paypal API & AJAX

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');

paypal.Button.render({
  // Configure environment
  env: 'sandbox',
  client: { 
    sandbox: 'ATfB9XPcq_Ok-8GUR1ne_bDcmeX7cJar_YKa0FsCRUgeeh4A2oVsrZPQ416utSbT5TVp3wda9C5HLYvt',
    production: 'demo_production_client_id'
  },
  // Customize button (optional)
  locale: 'en_US',
  style: {
    size: 'medium',
    color: 'gold',
    shape: 'pill',
  },

  // Enable Pay Now checkout flow (optional)
  commit: true,

  // Set up a payment
  payment: function(data, actions) {
    return actions.payment.create({
      transactions: [{
        amount: {
          total: '{{ price }}',
          currency: 'USD'
        }
      }]
    });
  },

  // Execute the payment

  onAuthorize: function(data, actions) {
    return actions.payment.execute().then(function() {
      // Show a confirmation message to the buyer
      $.ajax({
          type:'POST',
          url : "{% url 'payment' %}",
          beforeSend: function(request){
              request.setRequestHeader('X-CSRFToken', csrftoken)
          },
          data: JSON.stringify({'isPaid' : true}),
          success : function(data) {
              window.location.href ='/payment/'
          }
      })
    });
  }
}, '#paypal-button');


//Responsive navigation menu toggle
const menuBtn = document.querySelector(".nav-menu-btn");
const closeBtn = document.querySelector(".nav-close-btn");
const navigation = document.querySelector(".navigation");
const navItems = document.querySelectorAll(".nav-items a");

menuBtn.addEventListener("click", () => {
  navigation.classList.add("active");
});

closeBtn.addEventListener("click", () => {
  navigation.classList.remove("active");
});

navItems.forEach((navItem) => {
  navItem.addEventListener("click", () => {
      navigation.classList.remove("active");
  });
});

