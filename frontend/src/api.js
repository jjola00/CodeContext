const API_BASE_URL = process.env.REACT_APP_API_URL;

export const fetchMetrics = async () => {
  const response = await fetch(`${API_BASE_URL}/metrics`);
  return response.json();
};

export const sendAction = async (action) => {
  await fetch(`${API_BASE_URL}/${action}`, { method: "POST" });
};