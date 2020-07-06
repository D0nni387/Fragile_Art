let stripe_public_key = $('#id_stripe_public_key').text().slice(1,-1);
let client_secret = $('#id_client_secret').text().slice(1,-1);
let stripe = Stripe(stripe_public_key);
let elements = stripe.elements();
let card = elements.create('card');


// stripe default style element
var style = {
    base: {
      color: '#32325d',
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif',
      fontSmoothing: 'antialiased',
      fontSize: '16px',
      '::placeholder': {
        color: '#aab7c4'
      },
      ':-webkit-autofill': {
        color: '#32325d',
      },
    },
    invalid: {
      color: '#fa755a',
      iconColor: '#fa755a',
      ':-webkit-autofill': {
        color: '#fa755a',
      },
    }
  };

card.mount('#card-element', {style:style});