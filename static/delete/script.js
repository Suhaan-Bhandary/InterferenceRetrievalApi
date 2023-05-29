const deleteButton = document.getElementById("deleteButton");

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