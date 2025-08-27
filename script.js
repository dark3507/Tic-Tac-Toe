
        let player = "X";
        let gameOver = false;
        const cells = document.querySelectorAll(".cell");
        const turnLabel = document.getElementById("turn");
        const confettiCanvas = document.getElementById("confetti");
        const ctx = confettiCanvas.getContext("2d");
        let confettiParticles = [];

        function resizeCanvas() {
            confettiCanvas.width = window.innerWidth;
            confettiCanvas.height = window.innerHeight;
        }
        window.addEventListener('resize', resizeCanvas);
        resizeCanvas();

        function createConfetti() {
            for(let i = 0; i < 150; i++) {
                confettiParticles.push({
                    x: Math.random() * confettiCanvas.width,
                    y: Math.random() * confettiCanvas.height - confettiCanvas.height,
                    r: Math.random() * 6 + 4,
                    d: Math.random() * 30,
                    color: `hsl(${Math.random() * 360}, 100%, 50%)`,
                    tilt: Math.random() * 10 - 10
                });
            }
        }

        function drawConfetti() {
            ctx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
            confettiParticles.forEach(p => {
                ctx.beginPath();
                ctx.lineWidth = p.r;
                ctx.strokeStyle = p.color;
                ctx.moveTo(p.x + p.tilt, p.y);
                ctx.lineTo(p.x + p.tilt + p.r / 2, p.y + p.r);
                ctx.stroke();
            });
            updateConfetti();
        }

        function updateConfetti() {
            confettiParticles.forEach(p => {
                p.y += Math.cos(p.d) + 2 + p.r/2;
                p.x += Math.sin(p.d);
                if (p.y > confettiCanvas.height) {
                    p.y = -10;
                    p.x = Math.random() * confettiCanvas.width;
                }
            });
        }

        function startConfetti() {
            createConfetti();
            const confettiInterval = setInterval(drawConfetti, 20);
            setTimeout(() => {
                clearInterval(confettiInterval);
                confettiParticles = [];
                ctx.clearRect(0, 0, confettiCanvas.width, confettiCanvas.height);
            }, 4000);
        }

        function checkWinner() {
            const winCombos = [
                [[0,0],[0,1],[0,2]],
                [[1,0],[1,1],[1,2]],
                [[2,0],[2,1],[2,2]],
                [[0,0],[1,0],[2,0]],
                [[0,1],[1,1],[2,1]],
                [[0,2],[1,2],[2,2]],
                [[0,0],[1,1],[2,2]],
                [[0,2],[1,1],[2,0]]
            ];
            for (let combo of winCombos) {
                const [a,b,c] = combo;
                const cellA = document.querySelector(`.cell[data-row='${a[0]}'][data-col='${a[1]}']`);
                const cellB = document.querySelector(`.cell[data-row='${b[0]}'][data-col='${b[1]}']`);
                const cellC = document.querySelector(`.cell[data-row='${c[0]}'][data-col='${c[1]}']`);
                if (cellA.textContent && cellA.textContent === cellB.textContent && cellA.textContent === cellC.textContent) {
                    return true;
                }
            }
            return false;
        }

        function handleClick(e) {
            if (gameOver) return;
            const cell = e.target;
            if (cell.textContent === "") {
                cell.textContent = player;
                cell.style.color = player === "X" ? "#36D7B7" : "#F4D03F";

                if (checkWinner()) {
                    turnLabel.textContent = `¡Ganó ${player}!`;
                    startConfetti();
                    gameOver = true;
                    return;
                }
                if ([...cells].every(c => c.textContent !== "")) {
                    turnLabel.textContent = "¡Empate!";
                    gameOver = true;
                    return;
                }
                player = player === "X" ? "O" : "X";
                turnLabel.textContent = `Turno: ${player}`;
            }
        }

        cells.forEach(cell => cell.addEventListener("click", handleClick));

        document.getElementById("reset").addEventListener("click", () => {
            cells.forEach(cell => {
                cell.textContent = "";
                cell.style.color = "";
            });
            player = "X";
            gameOver = false;
            turnLabel.textContent = `Turno: ${player}`;
        });
 
