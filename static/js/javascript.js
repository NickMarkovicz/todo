document.addEventListener("DOMContentLoaded", function() {
  function ConfirmDeletion() {
      if (confirm('Do you really want to delete this note?')) {
          alert('OK')
      }
  }

  const button = document.getElementById("delete-button");

  button.addEventListener("click", ConfirmDeletion);
});
