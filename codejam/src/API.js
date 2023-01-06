import React, { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";
import axios from "axios";
import { db } from "./firebase";
import { collection, addDoc } from "firebase/firestore";

function FoodItems() {
  const [isLoading, setLoading] = useState(true);
  const [item, setItem] = useState();

  const [FoodItem, setFoodItem] = useState("");
  const handleFavorite = async (e) => {
    e.preventDefault();

    // if (FoodItem !== "") {
        await addDoc(collection(db, "favorites"), {
            id:e.currentTarget.value
        });
        alert("added to favorite")
    //     setSubject("");
    // }
  };

  useEffect(() => {
    axios
      .get(
        "https://api.spoonacular.com/food/products/search?query=pizza&apiKey=6e33da02ee8c43f08865c768c22e6114"
      )
      .then((response) => {
        setItem(response.data.products);
        setLoading(false);
      });
  }, []);

  if (isLoading) {
    return <div className="App">Loading...</div>;
  }

  return (
    <div className="container mt-5">
      <div className="row d-flex justify-content-center">
        {item.map(function (e) {
          return (
            <Card style={{ width: "18rem", margin: "5px" }}>
              <Card.Img variant="top" src={e.image} />
              <Card.Body>
                <Card.Title>{e.title}</Card.Title>
                <Card.Text>
                  Some quick example text to build on the card title and make up
                  the bulk of the card's content.
                </Card.Text>
                <Button
                  variant="primary"
                  className="d-block m-auto"
                  value={e.id}
                  onClick={handleFavorite}
                >
                  Add to favorite
                </Button>
              </Card.Body>
            </Card>
          );
        })}
      </div>
    </div>
  );
}
export default FoodItems;
