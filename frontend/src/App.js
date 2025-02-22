import React, { useState, useEffect } from "react";
import { fetchMetrics, startCollector, stopCollector } from "./api";
import Dashboard from "./components/Dashboard";
import MetricsTable from "./components/MetricsTable";
import Navbar from "./components/Navbar";

const App = () => {
  const [metricsHistory, setMetricsHistory] = useState([]); // For metrics history
  const [liveMetrics, setLiveMetrics] = useState([]); // For live metrics (max 6 entries)
  const [isCollectorRunning, setIsCollectorRunning] = useState(false); // Track collector status

  // Fetch metrics history on component mount
  useEffect(() => {
    const loadMetricsHistory = async () => {
      const data = await fetchMetrics();
      setMetricsHistory(data);
    };
    loadMetricsHistory();
  }, []);

  // Function to toggle the collector on/off
  const handleToggleCollector = async () => {
    try {
      if (isCollectorRunning) {
        await stopCollector(); // Stop the collector
        setLiveMetrics([]); // Clear live metrics
      } else {
        await startCollector(); // Start the collector
      }
      setIsCollectorRunning((prev) => !prev); // Toggle the running state
    } catch (error) {
      console.error("Failed to toggle collector:", error);
    }
  };

  // Poll for new metrics when the collector is running
  useEffect(() => {
    let interval;
    if (isCollectorRunning) {
      // Poll for new metrics every 5 seconds
      interval = setInterval(async () => {
        const data = await fetchMetrics();
        setLiveMetrics((prevMetrics) => {
          const newMetrics = [data[0], ...prevMetrics]; // Add the latest metric to the beginning
          return newMetrics.slice(0, 6); // Keep only the latest 6 metrics
        });
      }, 5000);
    }

    return () => clearInterval(interval); // Cleanup on unmount or when collector stops
  }, [isCollectorRunning]);

  return (
    <div style={styles.app}>
      <Navbar />
      <div style={styles.content}>
        <MetricsTable metrics={metricsHistory} />
        <button onClick={handleToggleCollector} style={styles.button}>
          {isCollectorRunning ? "Stop Viewing" : "View Live Metrics"}
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