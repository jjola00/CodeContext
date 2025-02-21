//api.js
const API_BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

export const fetchMetrics = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/metrics`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return response.json();
  } catch (error) {
    console.error("Failed to fetch metrics:", error);
    throw error;
  }
};