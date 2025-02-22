const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL;

export const fetchMetrics = async () => {
  try {
    const response = await fetch(`${API_BASE_URL}/metrics`);
    if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
    return await response.json();
  } catch (error) {
    console.error("Failed to fetch metrics:", error);
    return []; 
  }
};
