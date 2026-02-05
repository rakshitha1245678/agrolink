import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";

function BuyerDashboard() {
  const navigate = useNavigate();
  const [products, setProducts] = useState([]);

  useEffect(() => {
    API.get("/product/all")
      .then((res) => setProducts(res.data))
      .catch(() => alert("Failed to load products"));
  }, []);

  const logout = () => {
    localStorage.clear();
    navigate("/");
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2>🛒 Buyer Dashboard</h2>

      <h3>Available Products</h3>

      {products.map((p) => (
        <div key={p.id} style={{ marginBottom: "10px" }}>
          <b>{p.name}</b> — ₹{p.price} (Qty: {p.quantity})
        </div>
      ))}

      <br />
      <button onClick={logout}>Logout</button>
    </div>
  );
}

export default BuyerDashboard;
