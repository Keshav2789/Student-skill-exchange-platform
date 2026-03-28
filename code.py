<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Student Skill Exchange</title>

<style>
*{margin:0;padding:0;box-sizing:border-box;}

body{
    font-family:Arial;
    background:#f4f6f9;
    color:#333;
}

/* DARK MODE */
.dark-mode{background:#222;color:white;}
.dark-mode .card{background:#333;color:white;}
.dark-mode .header{background:linear-gradient(135deg,#000,#444);}

/* CONTAINER */
.container{max-width:1200px;margin:auto;padding:20px;}

/* HEADER */
.header{
    background:linear-gradient(135deg,#4facfe,#00f2fe);
    color:white;
    text-align:center;
    padding:2rem;
    border-radius:10px;
}

/* CARD */
.card{
    background:white;
    padding:20px;
    margin-top:20px;
    border-radius:10px;
    box-shadow:0 4px 10px rgba(0,0,0,0.08);
}

/* GRID */
.grid{display:grid;gap:20px;}
.grid-3{grid-template-columns:1fr;}

@media(min-width:600px){
.grid-3{grid-template-columns:repeat(2,1fr);}
}

@media(min-width:900px){
.grid-3{grid-template-columns:repeat(3,1fr);}
}

/* BUTTON */
.btn{
    padding:10px 20px;
    background:#007bff;
    color:white;
    border:none;
    border-radius:20px;
    cursor:pointer;
    margin:5px;
}
.btn:hover{background:#0056b3;}

/* FORM */
input, textarea{
    width:100%;
    padding:10px;
    margin:8px 0;
}

/* MODAL */
.modal{
    display:none;
    position:fixed;
    top:0;left:0;
    width:100%;height:100%;
    background:rgba(0,0,0,0.6);
}

.modal-content{
    background:rgba(255, 255, 255, 0.908);
    padding:20px;
    width:300px;
    margin:100px auto;
    border-radius:10px;
    text-align:center;
}

.close{
    float:right;
    cursor:pointer;
}

.dark-mode .modal-content{
    background:#333;
    color:white;
}
</style>
</head>

<body>

<div class="container">

<header class="header">
    <h1>Student Skill Exchange</h1>
    <p id="welcomeText">Learn, Teach & Grow Together</p>
</header>

<!-- AUTH BUTTONS -->
<div style="text-align:right;">
    <button class="btn" onclick="openModal()">Login / Signup</button>
    <button class="btn" id="logoutBtn" style="display:none;" onclick="logout()">Logout</button>
</div>

<!-- ABOUT -->
<div class="card">
    <h2>About Platform</h2>
    <p>Exchange skills with students and grow together.</p>
</div>

<!-- SKILLS -->
<div class="card">
    <h2>Skills</h2>
    <div class="grid grid-3" id="skillsContainer">
        <div class="card">Programming</div>
        <div class="card">Design</div>
        <div class="card">AI</div>
    </div>
</div>

<!-- CTA -->
<div class="card" id="ctaSection">
    <h2>Start Learning</h2>
</div>

<!-- CONTACT FORM -->
<div class="card">
    <h2>Contact</h2>
    <form id="contactForm">
        <input type="text" name="name" required placeholder="Name">
        <input type="email" name="email" required placeholder="Email">
        <textarea name="message" required placeholder="Message"></textarea>
        <button class="btn">Submit</button>
    </form>
</div>

</div>

<!-- MODAL -->
<div id="authModal" class="modal">
<div class="modal-content">
<span class="close" onclick="closeModal()">X</span>

<h2 id="formTitle">Login</h2>

<input type="email" id="email" placeholder="Email">
<input type="password" id="password" placeholder="Password">

<p id="errorMsg" style="color:red;"></p>

<button class="btn" onclick="handleAuth()">Submit</button>

<p onclick="toggleForm()" style="cursor:pointer;color:blue;">
Switch Login / Signup
</p>

</div>
</div>

<script>


document.addEventListener('DOMContentLoaded', ()=>{
    const btn=document.createElement('button');
    btn.textContent="Toggle Theme";
    btn.className="btn";
    btn.onclick=()=>document.body.classList.toggle('dark-mode');
    document.querySelector('.header').appendChild(btn);

    updateUI();
});

const loadBtn=document.createElement('button');
loadBtn.textContent="Load Skills";
loadBtn.className="btn";

loadBtn.onclick=()=>{
    const skills=["Cyber Security","Blockchain","Data Science"];
    const container=document.getElementById('skillsContainer');

    skills.forEach(s=>{
        const div=document.createElement('div');
        div.className="card";
        div.textContent=s;
        container.appendChild(div);
    });

    loadBtn.disabled=true;
};

document.getElementById('ctaSection').appendChild(loadBtn);

document.getElementById('contactForm').onsubmit=(e)=>{
    e.preventDefault();

    const email=e.target.email.value;

    if(/\S+@\S+\.\S+/.test(email)){
        localStorage.setItem('formData', email);
        alert("Saved ✅");
    }else{
        alert("Invalid Email ❌");
    }
};

let isLogin=true;

function openModal(){authModal.style.display="block";}
function closeModal(){authModal.style.display="none";}

function toggleForm(){
    isLogin=!isLogin;
    formTitle.textContent=isLogin?"Login":"Signup";
    errorMsg.textContent="";
}

function handleAuth(){
    const email=document.getElementById('email').value;
    const password=document.getElementById('password').value;

    if(!email || !password){
        errorMsg.textContent="Fill all fields";
        return;
    }

    let users=JSON.parse(localStorage.getItem('users'))||[];

    if(isLogin){
        const user=users.find(u=>u.email===email && u.password===password);
        if(user){
            localStorage.setItem('loggedUser',email);
            closeModal();
            updateUI();
        }else{
            errorMsg.textContent="Invalid credentials";
        }
    }else{
        users.push({email,password});
        localStorage.setItem('users',JSON.stringify(users));
        errorMsg.textContent="Signup success!";
    }
}

function logout(){
    localStorage.removeItem('loggedUser');
    updateUI();
}

function updateUI(){
    const user=localStorage.getItem('loggedUser');

    if(user){
        welcomeText.textContent="Welcome "+user;
        logoutBtn.style.display="inline-block";
    }else{
        welcomeText.textContent="Learn, Teach & Grow Together";
        logoutBtn.style.display="none";
    }
}

</script>

</body>
</html>
