import React, { useEffect, useState } from "react";
import MetricsTable from "./MetricsTable";
import Controls from "./Controls";

function Dashboard() {
  const [metrics, setMetrics] = useState([]);

  useEffect(() => {
    fetch("/metrics")
      .then((res) => res.json())
      .then((data) => setMetrics(data));
  }, []);

  return (
    <div>
      <h1>System Metrics Dashboard</h1>
      <MetricsTable metrics={metrics} />
      <Controls />
    </div>
  );
}

export default Dashboard;
