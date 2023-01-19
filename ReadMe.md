### Prerequisites:

- create a virtual env
  'python3 -m venv myenv'
- activate virtual environment
  'source <venv>/bin/activate' -- bash/zsh --
- install requirements
  'pip install -r requirements.txt'
  
### Create an image

- 'docker build -t <image_name> .'

### Stand up the container and see the result in output log

- 'docker run -d -p 8080:8080 <image:latest>'

### run as kubernetes pod & run service

- 'kubectl apply -f chatgpt.yaml'
- 'kubectl apply -f chatgpt-service.yaml'
