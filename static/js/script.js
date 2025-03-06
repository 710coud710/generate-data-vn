// script.js
function fetchRandomUser() {
    axios.get('/api/random-user')
        .then(response => {
            const data = response.data;
            document.getElementById("full_name").textContent = data.full_name;
            document.getElementById("gender").textContent = data.gender;
            document.getElementById("date_of_birth").textContent = data.date_of_birth;
            document.getElementById("phone_number").textContent = data.phone_number;
            document.getElementById("email").textContent = data.email;
            document.getElementById("cccd").textContent = data.cccd;
            document.getElementById("address").textContent = data.address;
            document.getElementById("job").textContent = data.job;
            document.getElementById("nationality").textContent = data.nationality;
            document.getElementById("company").innerText = data.company;
            document.getElementById("salary").innerText = data.salary;
            // document.getElementById("cccd_issue_place").innerText = data.cccd_issue_place;
            document.getElementById("facebook").textContent = data.facebook;
        })
        .catch(error => {
            console.error("Lỗi khi lấy dữ liệu:", error);
        });
}

function copySingle(elementId) {
    let text = document.getElementById(elementId).textContent;
    navigator.clipboard.writeText(text).catch(err => {
        console.error("Lỗi sao chép:", err);
    });
}

function copyAll() {
    let text = "";
    document.querySelectorAll("#user-data span").forEach(span => {
        text += span.previousSibling.textContent + " " + span.textContent + "\n";
    });
    
    navigator.clipboard.writeText(text).then(() => {
        alert("Đã sao chép toàn bộ thông tin!");
    }).catch(err => {
        console.error("Lỗi sao chép:", err);
    });
}

// Tự động lấy dữ liệu lần đầu
fetchRandomUser();
