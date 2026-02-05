import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../services/api";

function FarmerDashboard() {
  const navigate = useNavigate();
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [quantity, setQuantity] = useState("");

  const addProduct = async () => {
    try {
      const payload = {
        name: name,
        price: Number(price),
        quantity: Number(quantity),
      };

      console.log("Sending product:", payload);

      await API.post("/product/add", payload);

      alert("Product added successfully");
      setName("");
      setPrice("");
      setQuantity("");
    } catch (err) {
      console.error("Add product error:", err.response?.data || err);
      alert("Failed to add product");
    }
  };

  const logout = () => {
    localStorage.clear();
    navigate("/");
  };

  return (
    <div style={{ padding: "40px" }}>
      <h2>👨‍🌾 Farmer Dashboard</h2>

      <h3>Add Product</h3>

      <input
        placeholder="Product Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />
      <br /><br />

      <input
        placeholder="Price"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />
      <br /><br />

      <input
        placeholder="Quantity"
        value={quantity}
        onChange={(e) => setQuantity(e.target.value)}
      />
      <br /><br />

      <button onClick={addProduct}>Add Product</button>
      <br /><br />
      <button onClick={logout}>Logout</button>
    </div>
  );
}

export default FarmerDashboard;
