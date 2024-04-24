# DBRX-Bot

Welcome to the Iguazio Webinar: **Improving LLM Accuracy and Performance**

Ask me anything. For example:
- Write an essay about DBRX
- Analyze the pros and cons of using Artificial Intelligence in healthcare

---

### Example 1: Prompt Engineering

#### Baseline

```
Create a simple markdown form to collect demographic information from a web application user
```

#### Enhanced
- Step by step reasoning
- Provide instructions to tailor the output (multiple choices) 

```
Create a simple markdown form to collect detailed demographic information from a web application user.

The form should include radio buttons to allow the user to choose between common responses.

Explain your reasoning step by step, and compile the final result at the end.
```

---

### Example 2: RAG

Document Q&A: Provide a document and ask questions about it


```
You will be provided with a document and asked a question about it.

Answer the question from the document.
Document:
Farm Utility Exemption Notice
Act 1441 of 2013 provides an exemption from state and local sales taxes for electricity,
natural gas, and liquefied petroleum gas used by qualifying agricultural structures and
qualifying aquaculture and horticulture equipment beginning January 1, 2014.
The eligible utility must be separately metered and used only for the purpose of the
exemption. If a utility is sold for any other purpose, it will not be eligible for the exemption.
Before the exemption is allowed, the farmer seeking the exemption must obtain a
certificate from DFA to provide to the utility supplier.
Qualifying agricultural structures are defined as
A. A poultry or livestock facility used for commercial production, including without
limitation a broiler or turkey grow-out house, laying house, hatching unit,
nursery unit, breeding house, farrowing unit, and feed-out house;
B. A cattle or dairy facility, including without limitation a milking parlor, milk
collection unit, and refrigeration unit and
C. A greenhouse used for commercial production.
Horticulture means the initial production and cultivation of fruits, vegetables, tree nuts,
trees, shrubs, vines, and florists unless the cultivation of these items are at a retail or
wholesale facility from which the items are sold.
Aquaculture is defined as the active cultivation of domesticated fish that are spawned,
grown, managed, harvested, and marketed on an annual, semiannual, biennial, or short
term basis in waters that are confined within a pond, tank, or lake that is situated entirely
on the premises of a single owner and that, except under abnormal flood conditions, are
in no way connected by water or with any other flowing stream or body of water; or body
of water not situated on the premises of the owner.
Qualifying aquaculture or horticulture equipment includes:
A. A cooling unit, collection unit, or irrigation equipment used in a commercial
horticulture operation;
B. Equipment used to pump and aerate a pond used in a commercial aquaculture
operation; and
C. A holding and sorting tank used in a commercial aquaculture operation.
The forms to obtain the necessary certificate to provide to the utility suppliers are
available by contacting our office at 501-682-7105, Sales and Use Tax Section, P O Box
3566, Little Rock, AR 72203-3566 or are located in the Forms section on the Sales and
Use Tax page of the DFA website www.dfa.arkansas.gov .

Question: Is a greenhouse a qualifying agricultural structure?
```