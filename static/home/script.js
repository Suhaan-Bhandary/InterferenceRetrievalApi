// Variables
const updateButton = document.getElementById("updateButton");
const createForm = document.getElementById("createForm");
const deleteButton = document.getElementById("deleteButton");
const getButton = document.getElementById("dataButton");
const queryForm = document.getElementById("queryForm");

updateButton.addEventListener("click", () => {
  const class_name = document.getElementById("update_class_name").value;
  const sub_class_name = document.getElementById("update_sub_class_name").value;
  const relationship = document.getElementById("update_relationship").value;
  const domain = document.getElementById("update_domain").value;
  const range = document.getElementById("update_range").value;
  console.log(domain);
  const formData = {
    class_name,
    sub_class_name,
    relationship,
    domain,
    range,
  };

  console.log(formData);

  fetch("/api/owl/", {
    method: "PUT",
    body: JSON.stringify(formData),
    headers: { "Content-Type": "application/json" },
  }).then(() => {
    alert("Updated");
  });
});

createForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const formData = new FormData();
  const data_file = document.getElementById("create_date_file");
  formData.append("data_file", data_file.files[0]);

  fetch("/api/owl/", {
    method: "POST",
    body: formData,
  }).then(() => {
    alert("Created");
  });
});

deleteButton.addEventListener("click", () => {
  const class_name = document.getElementById("delete_class_name").value;
  const formData = { class_name };

  console.log(formData);

  fetch("/api/owl/", {
    method: "DELETE",
    body: JSON.stringify(formData),
    headers: { "Content-Type": "application/json" },
  }).then(() => {
    alert("Deleted");
  });
});

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
