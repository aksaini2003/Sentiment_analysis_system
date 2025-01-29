document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('analysisForm');
    const textInput = document.getElementById('textInput');
    const analyzeBtn = document.getElementById('analyzeBtn');
    const clearBtn = document.getElementById('clearBtn');
    const resultCard = document.getElementById('resultCard');
    const sentimentResult = document.getElementById('sentimentResult');
    const confidenceScore = document.getElementById('confidenceScore');
    const confidenceBar = document.getElementById('confidenceBar');
    const closeResult = document.getElementById('closeResult');
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toastMessage');
    const currentLength = document.getElementById('currentLength');
    const loadingOverlay = document.getElementById('loadingOverlay');

    // Character count update
    textInput.addEventListener('input', () => {
        const length = textInput.value.trim().length;
        currentLength.textContent = length;
        analyzeBtn.disabled = length === 0;
        
        if (length > 500) {
            textInput.value = textInput.value.substring(0, 500);
            showToast('Maximum character limit is 500');
        }
    });

    // Clear button
    clearBtn.addEventListener('click', () => {
        textInput.value = '';
        currentLength.textContent = '0';
        analyzeBtn.disabled = true;
        resultCard.classList.add('hidden');
    });

    // Close result card
    closeResult.addEventListener('click', () => {
        resultCard.classList.add('hidden');
    });

    // Toast notification
    function showToast(message, duration = 3000) {
        toastMessage.textContent = message;
        toast.classList.remove('hidden');
        
        setTimeout(() => {
            toast.classList.add('hidden');
        }, duration);
    }

    // Show loading overlay
    function showLoading() {
        loadingOverlay.classList.remove('hidden');
    }

    // Hide loading overlay
    function hideLoading() {
        loadingOverlay.classList.add('hidden');
    }

    // Get explanation based on confidence
    function getConfidenceExplanation(confidence) {
        const percent = (confidence * 100).toFixed(1);
        if (confidence >= 0.9) {
            return "The AI is very confident about this analysis.";
        } else if (confidence >= 0.7) {
            return "The AI is reasonably confident about this analysis.";
        } else if (confidence >= 0.5) {
            return "The AI shows moderate confidence in this analysis.";
        } else {
            return "The AI shows low confidence in this analysis. Consider rephrasing your text.";
        }
    }

    // Analyze sentiment
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const text = textInput.value.trim();
        
        if (!text) {
            showToast('Please enter some text to analyze');
            return;
        }

        try {
            // Show loading state
            showLoading();
            analyzeBtn.disabled = true;
            
            // Send request
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text }),
            });

            if (!response.ok) {
                throw new Error('Failed to analyze text');
            }

            const data = await response.json();
            
            if (data.error) {
                throw new Error(data.error);
            }
            
            // Update UI with results
            const isPositive = data.sentiment.toLowerCase().includes('positive');
            const confidence = data.confidence || 0;
            
            // Update sentiment result
            sentimentResult.innerHTML = `
                <div class="sentiment-icon">
                    <i class="fas ${isPositive ? 'fa-smile-beam' : 'fa-frown'} fa-2x"></i>
                </div>
                <div class="sentiment-text">${isPositive ? 'Positive Sentiment' : 'Negative Sentiment'}</div>
                <p class="sentiment-explanation">${getConfidenceExplanation(confidence)}</p>
            `;
            sentimentResult.className = `sentiment-result ${isPositive ? 'positive' : 'negative'}`;
            
            // Update confidence score with animation
            const confidencePercent = (confidence * 100).toFixed(0);
            confidenceScore.textContent = `${confidencePercent}%`;
            confidenceBar.style.width = `${confidencePercent}%`;
            
            // Show result card
            resultCard.classList.remove('hidden');
            
        } catch (error) {
            console.error('Error:', error);
            showToast(error.message || 'An error occurred while analyzing the text');
        } finally {
            // Reset states
            hideLoading();
            analyzeBtn.disabled = false;
        }
    });
});