// Site settings. Edit this file to connect the forms and the deposit link.
//
// forms: paste a form endpoint for each form. A free Formspree form works:
//   1. Sign up at formspree.io and create a form.
//   2. Copy its endpoint, which looks like https://formspree.io/f/abcdwxyz
//   3. Paste it between the quotes below.
// Until an endpoint is set, the form shows a "not connected yet" message
// instead of pretending it sent.
//
// depositLink: a Stripe Payment Link for the refundable founding-family
// deposit. Leave it empty to hide the deposit button.

window.WARMBOWL_CONFIG = {
  forms: {
    waitlist: "https://formspree.io/f/mzerzjpz",
    driver: "https://formspree.io/f/xoedvkae",
    restaurant: "https://formspree.io/f/mkjrgqwz"
  },
  depositLink: "",
  contactEmail: "warmbowlmeals@gmail.com"
};
