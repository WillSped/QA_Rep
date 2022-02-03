`strict mode`

const button = document.getElementById(`button`);
const input = document.getElementById(`input`);
const output = document.getElementById(`output`);


read = URL => {
    axios.get(URL)
    .then((response) => {
        output.innerHTML = JSON.stringify(response.data);
        }).catch((err) => {
            console.log(err);
        })
}

button.onclick = () => read(input.value);

create = URL => {
    axios.post(URL, {
        name : `Morpheus`,
        job : `Leader`
    })
      .then((response) => {
          output.innerHTML = JSON.stringify(response.data);
      }).catch((err) => {
          console.log(err);
      })
    
}

button.onclick = () => create(input.value);


create = URL => {
    axios.post(URL, {
        email: "eve.holt@reqres.in",
        password: "pistol"
    })
      .then((response) => {
          console.log("Registration Successful")
      }).catch((err) => {
          console.error("Request Failed");
      })
    
}

button.onclick = () => create(input.value);


create = URL => {
    axios.post(URL, {
        email: "eve.holt@reqres.in",
        password: "pistol"
    })
      .then((response) => {
          output.innerHTML = JSON.stringify("Login Successful");
      }).catch((err) => {
          console.error("Request Failed");
      })
    
}

button.onclick = () => create(input.value);

create = URL => {
    axios.post(URL, {
        email: "eve.holt@reqres.in",
        password: "cityslicka"
    })
      .then((response) => {
        output.innerHTML = JSON.stringify("Login Successful");
      }).catch((err) => {
          console.error("Request Failed");
      })
    
}

button.onclick = () => create(input.value);

