import React, { useState } from 'react';
import styled from 'styled-components';

const PageContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100%;
`;

const Card = styled.div`
  background-color: var(--color-background);
  border-radius: var(--border-radius-lg);
  box-shadow: var(--shadow-md);
  padding: var(--spacing-lg);
  margin-bottom: var(--spacing-lg);
`;

const WebhookUrl = styled.div`
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-md);
  padding: var(--spacing-md);
  font-family: monospace;
  margin: var(--spacing-md) 0;
  position: relative;
`;

const CopyButton = styled.button`
  position: absolute;
  top: var(--spacing-sm);
  right: var(--spacing-sm);
  background-color: var(--color-primary);
  color: white;
  padding: var(--spacing-xs) var(--spacing-sm);
  border-radius: var(--border-radius-sm);
  font-size: 12px;
  
  &:hover {
    background-color: var(--color-info);
  }
`;

const JsonExample = styled.pre`
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--border-radius-md);
  padding: var(--spacing-md);
  font-family: monospace;
  margin: var(--spacing-md) 0;
  overflow-x: auto;
`;

const AlertGeneratorForm = styled.form`
  display: flex;
  flex-direction: column;
  gap: var(--spacing-md);
`;

const FormGroup = styled.div`
  display: flex;
  flex-direction: column;
  gap: var(--spacing-xs);
`;

const Label = styled.label`
  font-weight: 500;
  color: var(--color-text-primary);
`;

const Input = styled.input<{ hasError?: boolean }>`
  height: 40px;
  padding: 0 var(--spacing-md);
  border: 1px solid ${props => props.hasError ? 'var(--color-error)' : 'var(--color-border)'};
  border-radius: var(--border-radius-md);
  background-color: var(--color-background);
  
  &:focus {
    outline: none;
    border-color: ${props => props.hasError ? 'var(--color-error)' : 'var(--color-primary)'};
    box-shadow: 0 0 0 2px ${props => props.hasError ? 'rgba(229, 62, 62, 0.2)' : 'rgba(62, 99, 221, 0.2)'};
  }
`;

const Select = styled.select<{ hasError?: boolean }>`
  height: 40px;
  padding: 0 var(--spacing-md);
  border: 1px solid ${props => props.hasError ? 'var(--color-error)' : 'var(--color-border)'};
  border-radius: var(--border-radius-md);
  background-color: var(--color-background);
  
  &:focus {
    outline: none;
    border-color: ${props => props.hasError ? 'var(--color-error)' : 'var(--color-primary)'};
    box-shadow: 0 0 0 2px ${props => props.hasError ? 'rgba(229, 62, 62, 0.2)' : 'rgba(62, 99, 221, 0.2)'};
  }
`;

const GenerateButton = styled.button`
  height: 40px;
  background-color: var(--color-primary);
  color: white;
  border-radius: var(--border-radius-md);
  font-weight: 500;
  
  &:hover {
    background-color: var(--color-info);
  }
  
  &:disabled {
    background-color: var(--color-text-disabled);
    cursor: not-allowed;
  }
`;

const OutputSection = styled.div`
  margin-top: var(--spacing-lg);
`;

const ErrorText = styled.span`
  color: var(--color-error);
  font-size: 12px;
  margin-top: 4px;
`;

const Notification = styled.div<{ type: 'success' | 'error' }>`
  padding: var(--spacing-sm) var(--spacing-md);
  background-color: ${props => props.type === 'success' ? 'var(--color-success)' : 'var(--color-error)'};
  color: white;
  border-radius: var(--border-radius-md);
  margin-bottom: var(--spacing-md);
  display: flex;
  align-items: center;
  justify-content: space-between;
`;

const CloseButton = styled.button`
  background: none;
  color: white;
  font-size: 16px;
  cursor: pointer;
`;

const StepsList = styled.ol`
  margin-left: var(--spacing-lg);
  margin-top: var(--spacing-md);
`;

const Step = styled.li`
  margin-bottom: var(--spacing-md);
  line-height: 1.5;
`;

const CodeSnippet = styled.code`
  background-color: var(--color-surface);
  padding: var(--spacing-xs) var(--spacing-sm);
  border-radius: var(--border-radius-sm);
  font-family: monospace;
  font-size: 14px;
`;

const ImagePlaceholder = styled.div`
  background-color: var(--color-surface);
  border: 1px dashed var(--color-border);
  border-radius: var(--border-radius-md);
  height: 200px;
  margin: var(--spacing-md) 0;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-secondary);
`;

interface FormErrors {
  symbol?: string;
  contracts?: string;
  price?: string;
}

export default function WebhookSetup() {
  const [formData, setFormData] = useState({
    symbol: 'BTCUSD',
    orderId: 'long',
    action: 'buy',
    contracts: '0.05',
    price: '64340.15',
    comment: 'Breakout'
  });
  
  const [formErrors, setFormErrors] = useState<FormErrors>({});
  const [generatedJson, setGeneratedJson] = useState('');
  const [notification, setNotification] = useState<{
    show: boolean;
    message: string;
    type: 'success' | 'error';
  }>({
    show: false,
    message: '',
    type: 'success'
  });
  
  const validateForm = () => {
    const errors: FormErrors = {};
    
    if (!formData.symbol.trim()) {
      errors.symbol = 'Symbol is required';
    }
    
    if (!formData.contracts.trim()) {
      errors.contracts = 'Contracts/shares is required';
    } else if (isNaN(parseFloat(formData.contracts)) || parseFloat(formData.contracts) <= 0) {
      errors.contracts = 'Must be a positive number';
    }
    
    if (!formData.price.trim()) {
      errors.price = 'Price is required';
    } else if (isNaN(parseFloat(formData.price)) || parseFloat(formData.price) <= 0) {
      errors.price = 'Must be a positive number';
    }
    
    setFormErrors(errors);
    return Object.keys(errors).length === 0;
  };
  
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
    
    // Clear error for this field when user types
    if (formErrors[name as keyof FormErrors]) {
      setFormErrors({
        ...formErrors,
        [name]: undefined
      });
    }
  };
  
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }
    
    const currentTime = new Date().getTime();
    
    const alertJson = {
      symbol: formData.symbol,
      strategy_order_id: formData.orderId,
      strategy_order_action: formData.action,
      strategy_order_contracts: parseFloat(formData.contracts),
      strategy_order_price: parseFloat(formData.price),
      strategy_order_comment: formData.comment,
      time: currentTime
    };
    
    setGeneratedJson(JSON.stringify(alertJson, null, 2));
  };
  
  const copyToClipboard = (text: string) => {
    navigator.clipboard.writeText(text)
      .then(() => {
        setNotification({
          show: true,
          message: 'Copied to clipboard!',
          type: 'success'
        });
        
        // Auto-hide notification after 3 seconds
        setTimeout(() => {
          setNotification(prev => ({ ...prev, show: false }));
        }, 3000);
      })
      .catch((err) => {
        console.error('Failed to copy: ', err);
        setNotification({
          show: true,
          message: 'Failed to copy to clipboard',
          type: 'error'
        });
      });
  };
  
  const closeNotification = () => {
    setNotification(prev => ({ ...prev, show: false }));
  };

  return (
    <PageContainer>
      <h1>Webhook Setup</h1>
      <p>Configure your TradingView alerts to send signals to your Viewzenix webhook endpoint.</p>
      
      {notification.show && (
        <Notification type={notification.type}>
          {notification.message}
          <CloseButton onClick={closeNotification}>×</CloseButton>
        </Notification>
      )}
      
      <Card>
        <h3>Your Webhook URL</h3>
        <p>Use this URL in your TradingView alert settings:</p>
        <WebhookUrl>
          https://api.viewzenix.com/webhook/tv/your-api-key
          <CopyButton onClick={() => copyToClipboard('https://api.viewzenix.com/webhook/tv/your-api-key')}>
            Copy
          </CopyButton>
        </WebhookUrl>
      </Card>
      
      <Card>
        <h3>TradingView Alert Format</h3>
        <p>Use the following JSON format in your TradingView alert message:</p>
        <JsonExample>{`{
  "symbol": "BTCUSD",
  "strategy_order_id": "long",
  "strategy_order_action": "buy",
  "strategy_order_contracts": 0.05,
  "strategy_order_price": 64340.15,
  "strategy_order_comment": "Breakout",
  "time": 1713746400000
}`}</JsonExample>
      </Card>
      
      <Card>
        <h3>TradingView Alert Generator</h3>
        <p>Use this tool to generate the correct alert format for your trading strategy.</p>
        
        <AlertGeneratorForm onSubmit={handleSubmit}>
          <FormGroup>
            <Label htmlFor="symbol">Symbol</Label>
            <Input 
              type="text" 
              id="symbol" 
              name="symbol" 
              value={formData.symbol} 
              onChange={handleInputChange} 
              placeholder="e.g. BTCUSD, AAPL, EUR/USD"
              hasError={!!formErrors.symbol}
            />
            {formErrors.symbol && <ErrorText>{formErrors.symbol}</ErrorText>}
          </FormGroup>
          
          <FormGroup>
            <Label htmlFor="orderId">Strategy Order ID</Label>
            <Input 
              type="text" 
              id="orderId" 
              name="orderId" 
              value={formData.orderId} 
              onChange={handleInputChange} 
              placeholder="e.g. long, short, entry, exit"
            />
          </FormGroup>
          
          <FormGroup>
            <Label htmlFor="action">Action</Label>
            <Select 
              id="action" 
              name="action" 
              value={formData.action} 
              onChange={handleInputChange}
            >
              <option value="buy">Buy</option>
              <option value="sell">Sell</option>
            </Select>
          </FormGroup>
          
          <FormGroup>
            <Label htmlFor="contracts">Contracts/Shares/Coins</Label>
            <Input 
              type="text" 
              id="contracts" 
              name="contracts" 
              value={formData.contracts} 
              onChange={handleInputChange} 
              placeholder="e.g. 0.05, 1, 100"
              hasError={!!formErrors.contracts}
            />
            {formErrors.contracts && <ErrorText>{formErrors.contracts}</ErrorText>}
          </FormGroup>
          
          <FormGroup>
            <Label htmlFor="price">Price</Label>
            <Input 
              type="text" 
              id="price" 
              name="price" 
              value={formData.price} 
              onChange={handleInputChange} 
              placeholder="e.g. 64340.15"
              hasError={!!formErrors.price}
            />
            {formErrors.price && <ErrorText>{formErrors.price}</ErrorText>}
          </FormGroup>
          
          <FormGroup>
            <Label htmlFor="comment">Comment</Label>
            <Input 
              type="text" 
              id="comment" 
              name="comment" 
              value={formData.comment} 
              onChange={handleInputChange} 
              placeholder="e.g. Breakout, Trend reversal"
            />
          </FormGroup>
          
          <GenerateButton type="submit">Generate Alert JSON</GenerateButton>
        </AlertGeneratorForm>
        
        {generatedJson && (
          <OutputSection>
            <h4>Generated Alert JSON</h4>
            <p>Copy this into your TradingView alert message:</p>
            <JsonExample>
              {generatedJson}
              <CopyButton onClick={() => copyToClipboard(generatedJson)}>
                Copy
              </CopyButton>
            </JsonExample>
          </OutputSection>
        )}
      </Card>
      
      <Card>
        <h3>How to Set Up TradingView Alerts</h3>
        <p>Follow these steps to configure your TradingView alerts to send signals to Viewzenix:</p>
        
        <StepsList>
          <Step>
            <strong>Open TradingView</strong> and navigate to your chart with the strategy or indicator you want to create alerts for.
          </Step>
          
          <Step>
            <strong>Create a new alert</strong> by clicking on the "Alert" button in the top toolbar, or by right-clicking on your chart and selecting "Add Alert".
            <ImagePlaceholder>
              TradingView Alert Button Screenshot (Coming Soon)
            </ImagePlaceholder>
          </Step>
          
          <Step>
            <strong>Set your alert conditions</strong> based on your trading strategy (price crossing a level, indicator signals, etc.)
          </Step>
          
          <Step>
            <strong>Configure the alert to use a webhook</strong> by selecting "Webhook URL" from the "Alert on" options.
          </Step>
          
          <Step>
            <strong>Enter your Viewzenix webhook URL</strong> that you can copy from the top of this page.
          </Step>
          
          <Step>
            <strong>In the "Message" field</strong>, paste the JSON format you generated with our tool above. Make sure it contains all the required fields.
            <ImagePlaceholder>
              TradingView Alert Settings Screenshot (Coming Soon)
            </ImagePlaceholder>
          </Step>
          
          <Step>
            <strong>Set your alert name and other options</strong> according to your preferences.
          </Step>
          
          <Step>
            <strong>Click "Create"</strong> to save your alert.
          </Step>
          
          <Step>
            <strong>Test your alert</strong> by manually triggering it or waiting for the conditions to be met. You should see the trade execution in the Logs tab of this dashboard.
          </Step>
        </StepsList>
        
        <p>For more detailed instructions, check out our <a href="#">Documentation</a> or <a href="#">Video Tutorial</a>.</p>
      </Card>
    </PageContainer>
  );
} 