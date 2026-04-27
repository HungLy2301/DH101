function initializeSearch(items) {
  const searchBox = document.getElementById('search-box');
  const noResults = document.getElementById('no-results');
  const grid = document.getElementById('grid');

  if (!searchBox) return;

  searchBox.addEventListener('input', (e) => {
    const query = e.target.value.toLowerCase().trim();
    const results = items.filter(item => 
      item.title.toLowerCase().includes(query) || 
      item.description.toLowerCase().includes(query)
    );

    // Clear grid
    if (grid) {
      grid.innerHTML = '';
    }

    // Show/hide no results
    if (results.length === 0 && query.length > 0) {
      if (noResults) noResults.style.display = 'block';
      if (grid) grid.style.display = 'none';
    } else {
      if (noResults) noResults.style.display = 'none';
      if (grid) grid.style.display = 'grid';
    }

    // Render results
    results.forEach(item => {
      if (grid) {
        grid.appendChild(createCard(item));
      }
    });

    // Show all if search is empty
    if (query.length === 0) {
      if (grid) grid.innerHTML = '';
      items.forEach(item => {
        if (grid) grid.appendChild(createCard(item));
      });
      if (noResults) noResults.style.display = 'none';
    }
  });
}

function createCard(item) {
  const card = document.createElement('div');
  card.className = 'card';
  card.innerHTML = `
    <div class="card-header">
      <div class="card-title">${item.title}</div>
      ${item.date ? `<div class="card-date">${item.date}</div>` : ''}
    </div>
    <div class="card-body">
      <div class="card-description">${item.description}</div>
      <div class="card-footer">
        <a href="${item.link}" class="btn">Read More</a>
      </div>
    </div>
  `;
  return card;
}
