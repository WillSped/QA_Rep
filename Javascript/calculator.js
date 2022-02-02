`use strict`
import * as DOM from './dom.js';

DOM.buttonAdd.onclick = () => addNumber(`${DOM.inputOne.value} + ${DOM.inputTwo.value} = ${+DOM.inputOne.value + +DOM.inputTwo.value}`);

DOM.buttonSub.onclick = () => subNumber(`${DOM.inputOne.value} - ${DOM.inputTwo.value} = ${DOM.inputOne.value - DOM.inputTwo.value}`);

DOM.buttonMult.onclick = () => multNumber(`${DOM.inputOne.value} * ${DOM.inputTwo.value} = ${DOM.inputOne.value * DOM.inputTwo.value}`);

DOM.buttonDiv.onclick = () => divNumber(`${DOM.inputOne.value} / ${DOM.inputTwo.value} = ${DOM.inputOne.value / DOM.inputTwo.value}`);

function addNumber(int){
    let out = document.createElement(`list_output`);
    out.innerHTML =int;
    DOM.outputList.appendChild(out)
}

function subNumber(int){
    let out = document.createElement(`list_output`);
    out.innerHTML =int;
    DOM.outputList.appendChild(out)
}

function multNumber(int){
    let out = document.createElement(`list_output`);
    out.innerHTML =int;
    DOM.outputList.appendChild(out)
}

function divNumber(int){
    let out = document.createElement(`list_output`);
    out.innerHTML =int;
    DOM.outputList.appendChild(out)
}
