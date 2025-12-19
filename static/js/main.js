// Show loading overlay on form submit and page navigation
document.addEventListener('DOMContentLoaded', function() {
    // Handle form submissions with loading overlay
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function() {
            const loadingOverlay = document.getElementById('loadingOverlay');
            if (loadingOverlay) {
                loadingOverlay.classList.remove('hidden');
            }
        });
    });
    
    // Add fade-in animation to content elements
    const contentElements = document.querySelectorAll('.fade-in-element');
    contentElements.forEach((element, index) => {
        // Stagger the animations for a nicer effect
        setTimeout(() => {
            element.classList.add('fade-in');
            element.style.opacity = '1';
        }, 100 * index);
    });
    
    // Enhanced file upload with drag and drop
    const dropZones = document.querySelectorAll('[id$="dropZone"]');
    dropZones.forEach(dropZone => {
        const fileInput = dropZone.querySelector('input[type="file"]');
        if (fileInput) {
            // Prevent default drag behaviors
            ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
                dropZone.addEventListener(eventName, preventDefaults, false);
                document.body.addEventListener(eventName, preventDefaults, false);
            });
            
            // Highlight drop area when item is dragged over it
            ['dragenter', 'dragover'].forEach(eventName => {
                dropZone.addEventListener(eventName, () => {
                    dropZone.classList.add('drop-zone-active');
                }, false);
            });
            
            ['dragleave', 'drop'].forEach(eventName => {
                dropZone.addEventListener(eventName, () => {
                    dropZone.classList.remove('drop-zone-active');
                }, false);
            });
            
            // Handle dropped files
            dropZone.addEventListener('drop', handleDrop, false);
            
            function preventDefaults(e) {
                e.preventDefault();
                e.stopPropagation();
            }
            
            function handleDrop(e) {
                const dt = e.dataTransfer;
                const files = dt.files;
                fileInput.files = files;
                
                // Update UI to show files selected
                if (files.length > 0) {
                    dropZone.innerHTML = `
                        <i class="fas fa-check-circle text-4xl text-green-500 mb-3"></i>
                        <p class="text-gray-600 mb-4">${files.length} fichier(s) sélectionné(s)</p>
                        <p class="text-gray-500 text-sm">Cliquez à nouveau pour changer les fichiers</p>
                    `;
                }
            }
        }
    });
    
    // Add loading overlay to all links for smooth page transitions
    const links = document.querySelectorAll('a[href]:not([target="_blank"]):not([href^="#"]):not([href^="javascript:"])');
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            // Don't show loader for anchor links or external links
            const url = this.getAttribute('href');
            const isExternal = url.startsWith('http') && !url.includes(window.location.hostname);
            
            if (!isExternal && !url.startsWith('#')) {
                const loadingOverlay = document.getElementById('loadingOverlay');
                if (loadingOverlay) {
                    loadingOverlay.classList.remove('hidden');
                }
            }
        });
    });
    
    // Button hover effects
    const buttons = document.querySelectorAll('button, .btn-hover');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', function() {
            this.classList.add('scale-105');
        });
        
        button.addEventListener('mouseleave', function() {
            this.classList.remove('scale-105');
        });
    });
});