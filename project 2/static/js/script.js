// validation

/// Creating variable with name in html

// login.html codes

const myform = document.getElementById("lgform")
const lguserid =  document.getElementById("lguserid");
const lgpassword = document.getElementById("lgpassword");

myform.addEventListener('submit',(e)=>{
    if(!validateInputs()){
        e.preventDefault();
    }
});

function validateInputs(){
    const lguser = lguserid.value.trim();
    const lgpass = lgpassword.value.trim();
    let success = true;
    // code for userid

    if (lguser === ""){
        success = false;
        setError (lguserid,"Please Enter a your userid");
    }
    else{
        setSuccess(lguserid);
    }

    //Code for password

    if (lgpass === ""){
        success = false;
        setError(lgpassword,"Please Enter  password");
    }
    else{
        setSuccess(lgpassword);
    }

    return success;
}

// Code for Error message

function setError(element, message){
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}

// Code for Success message

function setSuccess(element){
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

