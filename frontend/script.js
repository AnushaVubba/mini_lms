const API = "http://127.0.0.1:8000/api";

async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const res = await fetch(`${API}/token/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();

    if (data.access) {
        // store token
        localStorage.setItem("token", data.access);

        // redirect
        window.location.href = "courses.html";
    } else {
        document.getElementById("error").innerText = "Invalid login";
    }
}

async function loadCourses() {
    const token = localStorage.getItem("token");

    const res = await fetch(`${API}/courses/`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const courses = await res.json();

    const container = document.getElementById("courses");
    container.innerHTML = "";

    courses.forEach(course => {
        const div = document.createElement("div");
        div.innerHTML = `
            <h3>${course.title}</h3>
            <p>${course.description}</p>
            <hr>
        `;
        container.appendChild(div);
    });
}

function logout() {
    localStorage.removeItem("token");
    window.location.href = "index.html";
}

// Load all assignments
async function loadAssignments() {
    const res = await fetch(`${API}/courses/assignments/`);
    const data = await res.json();

    const container = document.getElementById("assignments");
    container.innerHTML = "";

    data.forEach(a => {
        container.innerHTML += `
            <div>
                <h3>${a.title}</h3>
                <p>${a.description}</p>
                <small>ID: ${a.id}</small>
                <hr>
            </div>
        `;
    });
}


// Submit assignment
async function submitAssignment() {
    const token = localStorage.getItem("token");

    const assignment = document.getElementById("assignmentId").value;
    const content = document.getElementById("content").value;

    await fetch(`${API}/courses/submissions/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            assignment: assignment,
            content: content
        })
    });

    alert("Submitted!");
    loadMySubmissions();
}


// Load student grades
async function loadMySubmissions() {
    const token = localStorage.getItem("token");

    const res = await fetch(`${API}/courses/my-submissions/`, {
        headers: {
            "Authorization": `Bearer ${token}`
        }
    });

    const data = await res.json();

    const container = document.getElementById("mySubmissions");
    container.innerHTML = "";

    data.forEach(s => {
        container.innerHTML += `
            <div>
                <p><b>Assignment:</b> ${s.assignment}</p>
                <p><b>Grade:</b> ${s.grade ?? "Not graded yet"}</p>
                <p><b>Feedback:</b> ${s.feedback ?? "-"}</p>
                <hr>
            </div>
        `;
    });
}
