document.addEventListener('DOMContentLoaded', function () {
    const modal = document.querySelector('#dynamicEmailModal');

    modal.addEventListener('show.bs.modal', function () {
        const dateTimeInput = modal.querySelector('input[type="datetime-local"]');
        
        

        if (dateTimeInput) {
            const now = new Date();
            const formattedDate = now.toISOString().slice(0, 16); // Formato "YYYY-MM-DDTHH:mm"
            dateTimeInput.value = formattedDate; // Asignar valor al input
        }
    });
});

