from carte_pizzeria import CartePizzeria, CartePizzeriaException
from pizza import Pizza
from unittest.mock import Mock
import pytest

def test_is_empty():
    cp = CartePizzeria()
    assert cp.is_empty()

def test_is_not_empty():
    pizza = Mock()
    cp = CartePizzeria()
    cp.add_pizza(pizza)
    assert not cp.is_empty()

def test_nb_pizza():
    p1 = Mock()
    p2 = Mock()
    cp = CartePizzeria()
    assert cp.nb_pizzas() == 0
    cp.pizzas = [p1]
    assert cp.nb_pizzas() == 1
    cp.pizzas = [p1, p2]
    assert cp.nb_pizzas() == 2

def test_remove_pizza():
    p = Mock(spec=Pizza)
    p.nom = "Cannibale"
    cp = CartePizzeria()
    cp.pizzas = [p]
    cp.remove_pizza("Cannibale")

def test_remove_not_existing_pizza():
    cp = CartePizzeria()
    with pytest.raises(CartePizzeriaException):
        cp.remove_pizza("Cannibale")
    



