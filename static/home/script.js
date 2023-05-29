// Variables
const createForm = document.getElementById("createForm");

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