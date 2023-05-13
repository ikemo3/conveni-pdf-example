import { createRoot } from "react-dom/client";
import React, { useEffect, useState } from "react";
import { faker } from "@faker-js/faker";

function Printer(props) {
  // 状態が変わってはいけないためuseStateを使う
  const [randomName, _] = useState(faker.person.fullName());
  const [pdfUrl, setPdfUrl] = useState(null);
  const [fetchData, setFetchData] = useState(false);

  useEffect(() => {
    if (fetchData) {
      async function fetchData() {
        const response = await fetch(
          `http://localhost:8000/request/${randomName}`
        );
        setPdfUrl(await response.text());
      }
      fetchData();
      setFetchData(false);
    }
  }, [fetchData]);

  return (
    <div>
      {randomName}
      <button className="fetchButton" onClick={() => setFetchData(true)}>
        取得
      </button>
      {pdfUrl && (
        <a href={pdfUrl} target="_blank" rel="noopener">
          PDF
        </a>
      )}
    </div>
  );
}

function ConvenienceStore(props) {
  const printers = Array(3).fill(0);
  return (
    <ul>
      {printers.map((_, index) => (
        <li key={index}>
          <Printer />
        </li>
      ))}
    </ul>
  );
}

function fetchAll() {
  const buttons = document.querySelectorAll("button.fetchButton");
  buttons.forEach((button) => {
    button.click();
  });
}

function App(props) {
  const stores = Array(10).fill(0);
  return (
    <div>
      <ul>
        {stores.map((_, index) => (
          <li key={index}>
            コンビニ{index}
            <ConvenienceStore />
          </li>
        ))}
      </ul>
      <button onClick={() => fetchAll()}>一括取得</button>
    </div>
  );
}

const root = createRoot(document.getElementById("app"));
root.render(<App />);
