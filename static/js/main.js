// Обработка выбора даты и времени для обновления доступных столиков
document.addEventListener('DOMContentLoaded', function() {
    const dateInput = document.getElementById('id_date');
    const timeSlotSelect = document.getElementById('id_time_slot');
    const tableSelect = document.getElementById('id_table');

    // Обновление доступных столиков при изменении даты
    if (dateInput) {
        dateInput.addEventListener('change', function() {
            updateAvailableTables();
        });
    }

    // Обновление доступных столиков при изменении времени
    if (timeSlotSelect) {
        timeSlotSelect.addEventListener('change', function() {
            updateAvailableTables();
        });
    }

    function updateAvailableTables() {
        const date = dateInput.value;
        const timeId = timeSlotSelect.value;

        if (!date || !timeId) {
            return;
        }

        fetch(`/api/available-tables/?date=${date}&time_slot=${timeId}`)
            .then(response => response.json())
            .then(data => {
                // Очищаем текущие опции
                tableSelect.innerHTML = '';

                // Добавляем новые опции
                data.tables.forEach(table => {
                    const option = document.createElement('option');
                    option.value = table.id;
                    option.textContent = `Столик ${table.number} (${table.capacity} мест)`;
                    tableSelect.appendChild(option);
                });
            })
            .catch(error => {
                console.error('Ошибка при получении доступных столиков:', error);
            });
    }
});