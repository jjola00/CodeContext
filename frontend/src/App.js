import React, { useState, useEffect } from "react";
import { fetchMetrics } from "./api";
import Dashboard from "./components/Dashboard";
import MetricsTable from "./components/MetricsTable";
import Navbar from "./components/Navbar";

const App = () => {
  const [metrics, setMetrics] = useState([]);

  useEffect(() => {
    const loadMetrics = async () => {
      const data = await fetchMetrics();
      setMetrics(data);
    };
    loadMetrics();
    const interval = setInterval(loadMetrics, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div style={styles.app}>
      <Navbar />
      <div style={styles.content}>
        <Dashboard metrics={metrics} />
        <MetricsTable metrics={metrics} />
      </div>
    </div>
  );
};

const styles = {
  app: {
    fontFamily: "Arial, sans-serif",
  },
  content: {
    padding: "20px",
  },
};

export default App;