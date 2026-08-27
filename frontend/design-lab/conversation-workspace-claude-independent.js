const systems = [
  {
    id: "technical-manuscript",
    name: "Technical Manuscript",
    note: "Reading room · no bubbles · calmer warm near-black"
  },
  {
    id: "studio-console",
    name: "Studio Console",
    note: "Same console · persistent state rail · compact technical density"
  },
  {
    id: "hybrid",
    name: "Hybrid",
    note: "Manuscript reading grammar + compact persistent state rail"
  }
];

const select = document.querySelector("#system-select");
const nav = document.querySelector("#system-nav");
const typefaceSelect = document.querySelector("#typeface-select");
const typefaceControl = document.querySelector("#typeface-control");

for (const system of systems) {
  const option = document.createElement("option");
  option.value = system.id;
  option.textContent = system.name;
  select.appendChild(option);

  const button = document.createElement("button");
  button.type = "button";
  button.className = "system-button";
  button.dataset.system = system.id;
  button.innerHTML = `<strong>${system.name}</strong><small>${system.note}</small>`;
  button.addEventListener("click", () => setSystem(system.id));
  nav.appendChild(button);
}

function setSystem(id) {
  document.documentElement.dataset.system = id;
  select.value = id;
  typefaceControl.hidden = id === "studio-console";
  document.querySelectorAll(".system-button").forEach((button) => {
    button.setAttribute("aria-pressed", String(button.dataset.system === id));
  });
}

select.addEventListener("change", (event) => setSystem(event.target.value));
typefaceSelect.addEventListener("change", (event) => {
  document.documentElement.dataset.typeface = event.target.value;
});

setSystem("technical-manuscript");
