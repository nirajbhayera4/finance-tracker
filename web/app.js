const currency = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
});

const form = document.querySelector("#expenseForm");
const amountInput = document.querySelector("#amount");
const categoryInput = document.querySelector("#category");
const formMessage = document.querySelector("#formMessage");
const totalSpent = document.querySelector("#totalSpent");
const entryCount = document.querySelector("#entryCount");
const categoryCount = document.querySelector("#categoryCount");
const expenseList = document.querySelector("#expenseList");
const categoryList = document.querySelector("#categoryList");

function renderExpenses(expenses) {
  expenseList.innerHTML = "";

  if (!expenses.length) {
    expenseList.innerHTML = '<li class="empty-state">No expenses recorded yet.</li>';
    return;
  }

  expenses
    .slice()
    .reverse()
    .forEach((expense) => {
      const item = document.createElement("li");
      item.className = "expense-item";
      item.innerHTML = `
        <span class="category-chip">${expense.category}</span>
        <strong>${currency.format(Number(expense.amount))}</strong>
      `;
      expenseList.appendChild(item);
    });

  gsap.from(".expense-item", {
    y: 16,
    opacity: 0,
    duration: 0.35,
    stagger: 0.04,
    ease: "power2.out",
  });
}

function renderCategories(categories) {
  const entries = Object.entries(categories).sort((a, b) => b[1] - a[1]);
  categoryList.innerHTML = "";

  if (!entries.length) {
    categoryList.innerHTML = '<div class="empty-state">Categories appear after your first expense.</div>';
    return;
  }

  entries.forEach(([category, amount]) => {
    const row = document.createElement("div");
    row.className = "category-row";
    row.innerHTML = `
      <span class="category-chip">${category}</span>
      <strong>${currency.format(Number(amount))}</strong>
    `;
    categoryList.appendChild(row);
  });
}

function renderDashboard(data) {
  const summary = data.summary;
  totalSpent.textContent = currency.format(summary.total_spent);
  entryCount.textContent = summary.count;
  categoryCount.textContent = Object.keys(summary.categories).length;
  renderExpenses(data.expenses);
  renderCategories(summary.categories);
}

async function loadExpenses() {
  const response = await fetch("/api/expenses");
  if (!response.ok) {
    throw new Error("Could not load expenses.");
  }
  renderDashboard(await response.json());
}

async function addExpense(event) {
  event.preventDefault();
  formMessage.textContent = "";

  const payload = {
    amount: amountInput.value,
    category: categoryInput.value,
  };

  const response = await fetch("/api/expenses", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  const data = await response.json();

  if (!response.ok) {
    formMessage.textContent = data.error || "Could not add expense.";
    gsap.fromTo(form, { x: -8 }, { x: 0, duration: 0.25, ease: "elastic.out(1, 0.4)" });
    return;
  }

  renderDashboard(data);
  form.reset();
  amountInput.focus();
  formMessage.textContent = "Saved to data/expenses.txt";

  gsap.fromTo(
    ".total-card",
    { scale: 0.98 },
    { scale: 1, duration: 0.35, ease: "back.out(2)" }
  );
}

function introAnimation() {
  gsap.from(".summary-panel, .expense-form, .expense-list-wrap, .category-panel", {
    y: 24,
    opacity: 0,
    duration: 0.7,
    stagger: 0.08,
    ease: "power3.out",
  });

}

form.addEventListener("submit", addExpense);
loadExpenses().then(introAnimation).catch((error) => {
  formMessage.textContent = error.message;
});
