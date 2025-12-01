function submitForm(e){
  e.preventDefault();
  const email = document.getElementById('email').value;
  document.getElementById('msg').textContent = 'Thanks — check your email for the guide (demo).';
  console.log('Lead captured:', email);
}
