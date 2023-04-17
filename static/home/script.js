// Variables
const updateButton = document.getElementById('updateButton');
const createForm = document.getElementById('createForm');
const deleteButton = document.getElementById('deleteButton');

updateButton.addEventListener('click', () => {
  const class_name = document.getElementById('update_class_name').value;
  const sub_class_name = document.getElementById('update_sub_class_name').value;
  const relationship = document.getElementById('update_relationship').value;

  const formData = {
    class_name,
    sub_class_name,
    relationship,
  };

  console.log(formData);

  fetch('/api/owl/', {
    method: 'PUT',
    body: JSON.stringify(formData),
    headers: { 'Content-Type': 'application/json' },
  }).then(() => {
    alert('Updated');
  });
});

createForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const formData = new FormData();
  const data_file = document.getElementById('create_date_file');
  formData.append('data_file', data_file.files[0]);

  fetch('/api/owl/', {
    method: 'POST',
    body: formData,
  }).then(() => {
    alert('Created');
  });
});

deleteButton.addEventListener('click', () => {
  const class_name = document.getElementById('delete_class_name').value;
  const formData = { class_name };

  console.log(formData);

  fetch('/api/owl/', {
    method: 'DELETE',
    body: JSON.stringify(formData),
    headers: { 'Content-Type': 'application/json' },
  }).then(() => {
    alert('Deleted');
  });
});
