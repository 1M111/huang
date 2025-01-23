document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchBtn = document.getElementById('searchBtn');
    const hotSearchList = document.getElementById('hotSearchList');

    // 搜索功能
    function performSearch() {
        const searchTerm = searchInput.value.trim();
        if (searchTerm) {
            window.location.href = `https://www.baidu.com/s?wd=${encodeURIComponent(searchTerm)}`;
        }
    }

    // 绑定搜索按钮点击事件
    searchBtn.addEventListener('click', performSearch);

    // 绑定回车键搜索
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            performSearch();
        }
    });

    // 获取热搜榜数据
    async function fetchHotSearch() {
        try {
            const response = await fetch('/api/hot-search');
            const data = await response.json();
            renderHotSearch(data);
        } catch (error) {
            console.error('获取热搜失败:', error);
        }
    }

    // 渲染热搜榜
    function renderHotSearch(data) {
        hotSearchList.innerHTML = '';
        data.forEach((item, index) => {
            const hotItem = document.createElement('div');
            hotItem.className = 'hot-item';
            
            const indexSpan = document.createElement('span');
            indexSpan.className = `hot-index ${index < 3 ? 'top3' : ''}`;
            indexSpan.textContent = index + 1;

            const contentDiv = document.createElement('div');
            contentDiv.className = 'hot-content';

            const titleDiv = document.createElement('div');
            titleDiv.className = 'hot-title';
            titleDiv.textContent = item.title;

            const descDiv = document.createElement('div');
            descDiv.className = 'hot-description';
            descDiv.textContent = item.description;

            contentDiv.appendChild(titleDiv);
            contentDiv.appendChild(descDiv);

            hotItem.appendChild(indexSpan);
            hotItem.appendChild(contentDiv);

            hotItem.addEventListener('click', () => {
                searchInput.value = item.title;
                performSearch();
            });

            hotSearchList.appendChild(hotItem);
        });
    }

    // 初始获取热搜数据
    fetchHotSearch();

    // 每隔5分钟更新一次热搜
    setInterval(fetchHotSearch, 5 * 60 * 1000);
});
