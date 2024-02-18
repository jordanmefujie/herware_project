const formFields = [
    {
        name: "name",
        label: "Name",
        type: "text",
        required: true,
    },
    {
        name: "email",
        label: "Email",
        type: "email",
        required: true,
    },
    {
        name: "username",
        label: "Username",
        type: "text",
        required: true,
    },
    {
        name: "password",
        label: "Password",
        type: "password",
        required: true,
    },
    {
        name: "dob",
        label: "Date of Birth",
        type: "date",
        required: true,
    },
    {
        name: "education",
        label: "Education",
        type: "select",
        options: [
            { label: "High School", value: "high_school" },
            { label: "Some College", value: "some_college" },
            { label: "Bachelor's Degree", value: "bachelors" },
            { label: "Master's Degree", value: "masters" },
            { label: "PhD", value: "phd" },
        ],
        required: true,
    },
    // Add other form fields as needed
];

const createHerwareForm = (
) => {
    const formContainer = document.getElementById("herwareFormContainer");

    for (const field of formFields) {
        const label = document.createElement("label");
        label.textContent = field.label;
        label.htmlFor = field.name;
        formContainer.appendChild(label);

        let input;

        switch (field.type) {
            case "text":
                input = document.createElement("input");
                input.type = "text";
                break;
            case "email":
                input = document.createElement("input");
                input.type = "email";
                break;
            case "date":
                input = document.createElement("input");
                input.type = "date";
                break;
            case "select":
                const select = document.createElement("select");
                field.options.
