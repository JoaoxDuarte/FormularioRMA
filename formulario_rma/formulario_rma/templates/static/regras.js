const checkIcon =
  '<svg stroke="green" class="pe-auto only-icon-small bi bi-info-circle-fill z-index-2 text-primary position-absolute top-50 end-0 translate-middle-y me-2 me-md-3" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check" viewBox="0 0 16 16"><path d="M10.97 4.97a.75.75 0 0 1 1.07 1.05l-3.99 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.267.267 0 0 1 .02-.022z"/></svg>';
const wrongIcon =
  '<svg stroke="red" class="pe-auto only-icon-small bi bi-info-circle-fill z-index-2 text-primary position-absolute top-50 end-0 translate-middle-y me-2 me-md-3" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x" viewBox="0 0 16 16"><path d="M4.646 4.646a.5.5 0 0 1 .708 0L8 7.293l2.646-2.647a.5.5 0 0 1 .708.708L8.707 8l2.647 2.646a.5.5 0 0 1-.708.708L8 8.707l-2.646 2.647a.5.5 0 0 1-.708-.708L7.293 8 4.646 5.354a.5.5 0 0 1 0-.708z"/></svg>';
const infoIcon =
  '<svg class="pe-auto only-icon-small bi bi-info-circle-fill z-index-2 text-primary position-absolute top-50 end-0 translate-middle-y me-2 me-md-3" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-info-circle" viewBox="0 0 16 16"><path d="M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z"/><path d="m8.93 6.588-2.29.287-.082.38.45.083c.294.07.352.176.288.469l-.738 3.468c-.194.897.105 1.319.808 1.319.545 0 1.178-.252 1.465-.598l.088-.416c-.2.176-.492.246-.686.246-.275 0-.375-.193-.304-.533L8.93 6.588zM9 4.5a1 1 0 1 1-2 0 1 1 0 0 1 2 0z"/></svg>';

class Regra {
  constructor(
    dependencies,
    text,
    rule,

  ) {
    this.dependencies = dependencies;
    this.text = text;
    this.rule = rule;
    this.nodes = this.dependencies.map((el) => {
      return document.getElementById(el);
    });

    this.tooltips = this.dependencies.map((el) => {
      return document.getElementById(el + "_tooltip");
    });
  }

  isValid() {
    //apply the rule in the integer values forom the nodes
    return this.rule(...this.nodes.map((input) => Number(input.value)));
  }
}

class RuleSet {
  constructor(rules) {
    this.rules = rules;

    //create a hash set for the rules in each node
    let rules_set = {};
    this.rules.forEach((rule) => {
      rule.dependencies.forEach((nodeId) => {
        if (rules_set[nodeId]) {
          rules_set[nodeId] = [...rules_set[nodeId], rule];
        } else {
          rules_set[nodeId] = [rule];
        }
      });
    });

    //A1 : [Regra1, Regra2]

    this.rules_set = rules_set;

    //Add the dependencies as a composite function
    Object.keys(rules_set).forEach((nodeId) => this.pre_process(nodeId));
  }

  verify_node(nodeId) {
    let approved = true;
    for (const rule of this.rules_set[nodeId]) {
      approved &= rule.isValid();
      //this is a binary OR operation, fancy right? 
      //You can actually break the code when something false happens. So you don't need to evaluate everything
      //This would be the way to lazyly do it. 
      //The problem is that you may want to know what rules broke, and this code is ready to do it.
    }

    return approved;
  }

  get_dependencies_for_node(nodeId) {
    let dependencies = [];
    for (const rule of this.rules_set[nodeId]) {
      dependencies = [...dependencies, ...rule.dependencies];
    }

    return dependencies.filter((e) => e != nodeId);
  }

  isValid() {
    let approved = true;
    for (const rule of this.rules) {
      approved &= rule.isValid();
      //this is a binary OR operation, fancy right? 
      //You can actually break the code when something false happens. So you don't need to evaluate everything
      //This would be the way to lazyly do it. 
      //The problem is that you may want to know what rules broke, and this code is ready to do it.
    }

    return approved;

  }

  pre_process(nodeId) {
    //Preprocessing tooltip
    let tooltip = document.getElementById(nodeId + "_tooltip");
    tooltip.title = this.rules_set[nodeId].map((el) => el.text).join("\n");
    tooltip.style.display = "block";
    tooltip.innerHTML = infoIcon;


    //Adding events
    let node = document.getElementById(nodeId);

    node.onchange = () => {
      const approved = this.verify_node(nodeId);
      if (approved) {
        this.positive_feedback(nodeId);
      } else {
        this.negative_feedback(nodeId);
      }

      //Verify each child. Notice that some rules will be evaluated two times. 
      //This code is not optimized
      this.get_dependencies_for_node(nodeId).forEach((dNodeId) => {
        if (this.verify_node(dNodeId)) {
          this.positive_feedback(dNodeId);
        } else {
          this.negative_feedback(dNodeId);
        }
      });
    };
  }

  negative_feedback(nodeId) {
    let tooltip = document.getElementById(nodeId + "_tooltip");
    tooltip.style.backgroundColor = "red";
    tooltip.style.color = "red";
    tooltip.innerHTML = wrongIcon;

    let node = document.getElementById(nodeId);

    node.style.color = "red";
  }
  positive_feedback(nodeId) {
    let tooltip = document.getElementById(nodeId + "_tooltip");

    tooltip.style.backgroundColor = "green";
    tooltip.style.color = "green";
    tooltip.innerHTML = checkIcon;

    let node = document.getElementById(nodeId);
    node.style.color = "black";
  }

}
