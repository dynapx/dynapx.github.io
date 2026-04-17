document.addEventListener("DOMContentLoaded", function() {
    initTypingEffect();
});

// 因为启用了 navigation.instant，页面是无刷新加载的，所以需要监听 document 专用的加载事件
document.addEventListener("DOMContentSwitch", function() {
    initTypingEffect();
});

function initTypingEffect() {
    const textElement = document.getElementById("typing-text");
    if (!textElement) return;

    const texts = ["探索代码的乐趣", "记录生活的点滴", "分享技术的成长"];
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typeSpeed = 100;

    function type() {
        const currentText = texts[textIndex];
        
        if (isDeleting) {
            textElement.textContent = currentText.substring(0, charIndex - 1);
            charIndex--;
            typeSpeed = 50; 
        } else {
            textElement.textContent = currentText.substring(0, charIndex + 1);
            charIndex++;
            typeSpeed = 150;
        }

        if (!isDeleting && charIndex === currentText.length) {
            isDeleting = true;
            typeSpeed = 1500; // 暂停一会再删除
        } else if (isDeleting && charIndex === 0) {
            isDeleting = false;
            textIndex = (textIndex + 1) % texts.length;
            typeSpeed = 500; // 打下一个词前的停顿
        }

        setTimeout(type, typeSpeed);
    }
    
    // 如果已经有内容了说明可能被重复调用，先清空
    if (!textElement.dataset.typingStarted) {
        textElement.dataset.typingStarted = true;
        textElement.textContent = '';
        type();
    }
}