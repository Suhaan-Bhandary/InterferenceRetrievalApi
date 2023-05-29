const updateButton = document.getElementById("updateButton");

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
  