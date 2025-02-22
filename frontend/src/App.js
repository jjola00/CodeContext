import React, { useState, useEffect } from "react";
import { fetchMetrics, startCollector } from "./api";
import Dashboard from "./components/Dashboard";
import MetricsTable from "./components/MetricsTable";
import Navbar from "./components/Navbar";

const App = () => {
  const [metricsHistory, setMetricsHistory] = useState([]); // For metrics history
  const [liveMetrics, setLiveMetrics] = useState([]); // For live metrics (max 5 entries)
  const [isCollectorRunning, setIsCollectorRunning] = useState(false); // Track collector status

  // Fetch metrics history on component mount
  useEffect(() => {
    const loadMetricsHistory = async () => {
      const data = await fetchMetrics();
      setMetricsHistory(data);
    };
    loadMetricsHistory();
  }, []);

  // Function to start the collector agent
  const handleStartCollector = async () => {
    try {
      await startCollector(); // Call the backend to start the collector
      setIsCollectorRunning(true);
    } catch (error) {
      console.error("Failed to start collector:", error);
    }
  };

  // Function to add a new live metric (and limit to 5 entries)
  const addLiveMetric = (metric) => {
    setLiveMetrics((prevMetrics) => {
      const newMetrics = [metric, ...prevMetrics]; // Add new metric to the beginning
      return newMetrics.slice(0, 5); // Keep only the latest 5 metrics
    });
  };

  return (
    <div style={styles.app}>
      <Navbar />
      <div style={styles.content}>
        <MetricsTable metrics={metricsHistory} />
        <button
          onClick={handleStartCollector}
          disabled={isCollectorRunning}
          style={styles.button}
        >
          {isCollectorRunning ? "Collector Running..." : "Start Collector"}
        </button>
        {isCollectorRunning && <Dashboard metrics={liveMetrics} />}
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
  button: {
    backgroundColor: "#3f51b5",
    color: "#ffffff",
    padding: "10px 20px",
    border: "none",
    borderRadius: "4px",
    cursor: "pointer",
    marginBottom: "20px",
  },
};

export default App;