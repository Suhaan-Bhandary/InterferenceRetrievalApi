const getButton = document.getElementById("dataButton");
const queryForm = document.getElementById("queryForm");

getButton.addEventListener("click", () => {
    console.log("Button clicked");
    fetch("/api/owl/")
      .then(() => {
        alert("Done");
      })
      .catch(() => {
        alert("Error");
      });
  });
  
  queryForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const user_text = document.getElementById("query").value;
    const body = { user_text };
  
    console.log(body);
  
    fetch("/api/query/", {
      method: "POST",
      body: JSON.stringify(body),
      headers: { "Content-Type": "application/json" },
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        document.getElementById("queryResult").innerText = "Result: " + data.data;
      })
      .catch(() => {
        alert("Error!!");
      });
  });
  