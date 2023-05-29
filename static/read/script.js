const getButton = document.getElementById("dataButton");
const queryForm = document.getElementById("queryForm");

const displayData = (data) => {
  const queryResult = document.getElementById("queryResult");
  queryResult.innerHTML = "";

  const resultText = document.createElement("h3");
  resultText.textContent = "Result";
  queryResult.appendChild(resultText);

  for (let i = 0; i < data.length; i++) {
    const hasAttribute__class_name = "class_name" in data[i];

    const result_block = document.createElement("div");
    result_block.className = "result_block";

    if (hasAttribute__class_name) {
      class_name = document.createElement("div");
      class_name.innerHTML = `<p>Class</p><p>${data[i].class_name}</p>`;
      class_name.className = "class_name";
      result_block.appendChild(class_name);

      parent_class_name = document.createElement("div");
      parent_class_name.innerHTML = `<p>Parent Class</p><p>${data[i].parent_class_name}</p>`;
      parent_class_name.className = "parent_class_name";
      result_block.appendChild(parent_class_name);

      sub_class_name = document.createElement("div");
      sub_class_name.innerHTML = `<p>Sub Class</p><p>${data[i].sub_class_name}</p>`;
      sub_class_name.className = "sub_class_name";
      result_block.appendChild(sub_class_name);

      // Attribute is an array
      // Attribute_name, Attribute_value
      attributes = document.createElement("div");
      const attributeText = document.createElement("p");
      attributeText.textContent = "Attributes";
      attributes.appendChild(attributeText);

      for (let k = 0; k < data[i].attribute.length; k++) {
        const element = data[i].attribute[k];
        attribute = document.createElement("div");
        attribute.innerHTML = `
          <div class="attribute">
            <p>Attribute Name: ${element["Attribute_name"]}</p>
            <p>Attribute Value: ${element["Attribute_value"]}</p>
          </div>
        `;

        attributes.appendChild(attribute);
      }
      result_block.appendChild(attributes);
    } else {
      relationship = document.createElement("div");
      relationship.innerHTML = `<p>Relationship</p><p>${data[i].relationship}</p>`;
      relationship.className = "relationship";
      result_block.appendChild(relationship);

      domain = document.createElement("div");
      domain.innerHTML = `<p>Domain</p><p>${data[i]["relationship-domain"]}</p>`;
      domain.className = "domain";
      result_block.appendChild(domain);

      range = document.createElement("div");
      range.innerHTML = `<p>Range</p><p>${data[i]["relationship-range"]}</p>`;
      range.className = "range";
      result_block.appendChild(range);
    }

    queryResult.appendChild(result_block);
  }
};

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

  fetch("/api/query/", {
    method: "POST",
    body: JSON.stringify(body),
    headers: { "Content-Type": "application/json" },
  })
    .then((response) => response.json())
    .then((jsonResponse) => {
      // console.log(jsonResponse);
      const data = jsonResponse.data;
      displayData(data);
    })
    .catch(() => {
      alert("Error!!");
    });
});
