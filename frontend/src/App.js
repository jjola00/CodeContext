// frontend/src/App.js
import React, { useEffect, useState } from "react";
import { fetchMetrics, sendAction } from "./api";
import Dashboard from "./components/Dashboard";
import MetricsTable from "./components/MetricsTable";
import Controls from "./components/Controls";

const App = () => {
  const [metrics, setMetrics] = useState([]);

  useEffect(() => {
    const loadMetrics = async () => {
      const data = await fetchMetrics();
      setMetrics(data);
    };
    loadMetrics();
  }, []);

  const handleAction = async (action) => {
    await sendAction(action);
    alert(`Action "${action}" sent successfully!`);
  };

  return (
    <div>
      <h1>System Monitor</h1>
      <Dashboard metrics={metrics} />
      <MetricsTable metrics={metrics} />
      <Controls onAction={handleAction} />
    </div>
  );
};

export default App;